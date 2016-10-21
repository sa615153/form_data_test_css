# -*- coding: utf-8 -*-

from database import Session

from flask_restful import reqparse
from flask_restful import abort
from flask_restful import Resource
from flask_restful import fields
from flask_restful import marshal_with

from qa_api.models import MajorTask
from qa_api.models import Machine
from qa_api.models import SubTask
from qa_api.models import SubtaskProperty
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from sqlalchemy import or_

import time

parser = reqparse.RequestParser()
parser.add_argument('task', type=str)
parser.add_argument('tracknumber', type=str)
parser.add_argument('status', type=str)


class AvailableTaskPCMatch(Resource):
    def sub_is_todo(x):
        if x.status == 0:
            return True
        else:
            return False

    def get(self):

        # 创建独立session,为互斥使用,贯彻整个get
        session = Session()

        # 将来要返回给dispatcher的初始“任务-机器”对 列表
        return_list = []

        ############################################
        ###lock using table machine
        ############################################

        # find idle machines
        idle_machine_list = session.query(Machine).with_lockmode('update').filter(Machine.status == 0).all()

        # find conclusion report type subtasks in subtask table
        conclusion_report_list = session.query(SubTask).filter(SubTask.name == 'report').all()

        # filter to figure out all windows machines to do report in idle machine list
        available_doreport_machine_list = filter(lambda x: True if x.label == 'windows' else False, idle_machine_list)

        # assign reports to idle windows machines
        for ival in range(0, len(conclusion_report_list) - 1):
            if ival < len(available_doreport_machine_list):
                return_list.append((conclusion_report_list[ival], available_doreport_machine_list[ival]))
                # remove target machine cos it has been assigned to do report
                idle_machine_list.remove(available_doreport_machine_list[ival])
                # end of report subtask assginment





                ####################################################################
                # process to assign normal subtasks by priority or by precondition #
                ####################################################################
        # get test2 to_do task
        todo_Test2_list = session.query(MajorTask). \
            filter((MajorTask.is_test2 == 1)). \
            filter(or_(MajorTask.status == 0, MajorTask.status == 1)). \
            all()

        for task in todo_Test2_list:
            # gather to_do subtasks
            todo_subtask_list = filter(lambda x: True if x.status == 0 else False, task.subtasks)
            for subtask in todo_subtask_list:
                # ignore report tasks for they have been assigned
                if subtask.name == "report":
                    continue

                # normal ones, check precondition
                pre = subtask.property.precondition
                if pre == "no":  # 无前提条件
                    pass  # assign this subtask

                else:
                    '''check the precondition subtask and if its done'''
                    prelist = filter(lambda x: True if x.name == pre else False, task.subtasks)
                    if prelist[0].status == 0 or prelist[0].status == 1:  # 前提条件未完成
                        continue  # 不分配此ｓｕｂｔａｓｋ
                    elif prelist[0].status == 2 and prelist[0].result == 'failed':
                        continue
                    else:
                        available_machine_list = filter(lambda x: True if x.label == subtask.property.label else False,
                                                        idle_machine_list)

                        pass  # assign this subtask

        # get test1&2 to_do task
        todo_Test2_list = session.query(MajorTask). \
            filter((MajorTask.is_test2 == 1)). \
            filter(or_(MajorTask.status == 0, MajorTask.status == 1)). \
            all()

        # get test1 to_do task
        todo_Test2_list = session.query(MajorTask). \
            filter((MajorTask.is_test2 == 1)). \
            filter(or_(MajorTask.status == 0, MajorTask.status == 1)). \
            all()

        # 空闲windows机器列表
        idle_quality_machines = session.query(Machine).with_lockmode('update').filter(Machine.status == 0,
                                                                                      Machine.label == 'windows').all()

        # 空闲linux机器列表
        idle_linux_compile_machines = session.query(Machine).with_lockmode('update').filter(Machine.status == 0,
                                                                                            Machine.label == 'linux').all()

        # 机器状态
        machine_dict = {'windows': idle_quality_machines, 'linux': idle_linux_compile_machines}

        # 空闲任务（todo doing）
        idle_task_list = session.query(MajorTask).filter(
            or_(MajorTask.status == 0, MajorTask.status == 1)).all()
        print("type of idle_task_list %s" % type(idle_task_list))

        def find_match(machine_dict):
            for major_task in idle_task_list:
                for subtask in filter(sub_is_todo, major_task.subtasks):
                    subtask_machine_label = session.query(SubtaskProperty).filter(
                        SubtaskProperty.subtask_name == subtask.name).all()
                    print("subtask_machine_label:%s" % type(subtask_machine_label[0]))
                    subtask_property = subtask_machine_label[0]
                    # print("KLKLK:%s" %temp.label)
                    if len(machine_dict[subtask_property.label]) == 0:  # this label no machine
                        continue
                    else:
                        target_machine = machine_dict[subtask_property.label].pop()  # get the target machine
                        print("target::::%s" % target_machine)
                        return (subtask, target_machine)
            return 0

        find_match_result = find_match(machine_dict)

        if find_match_result != 0:  # get available task machine match success
            '''
            # change the database
            # change the subtask.status from 0 to 1(todo to doing)
            # set subtask.machine_name with the target_machine.hostname
            # change the target_machine.machine_status from 0 to 1(idle to busy)
            # change MajorTask.status,,,before 0 now 1(todo to doing),,,before 1 now 1 or 2(doing to doing or done)
            '''

            # find_match_result[0].subtask_status = 1
            # find_match_result[0].machine_name = find_match_result[1].hostname
            # find_match_result[1].machine_status = 1
            #
            # cur_major = find_match_result[0].MajorTask
            #
            # if cur_major.task_status == 0:#before the Majortask is todo,change it to doing
            #     cur_major.task_status = 1
            #
            # elif cur_major.task_status == 1:#before the Majortask is doing, it is doing
            #     cur_major.task_status = 1#do nothing   password

            ############################################
            ###unlock using table machine
            ############################################

            # time.sleep(10)

            session.commit()
            subtask_list = find_match_result[0]
            machine_list = find_match_result[1]
            print("find***:%s" % find_match_result[0])
            print
            return {"task name:": subtask_list.major_task_track_number,
                    "subtask_type:": subtask_list.name,
                    "machine:": machine_list.IP}

        else:  # find_match_result == 0

            ############################################
            ###unlock using table machine
            ############################################

            session.commit()

            return {"task name:": None, "subtask_type:": None,
                    "machine:": None}

    def modify_machine_status(self, session, status, machine_list):
        pass

    def modify_subtask_table(self, session, status, subtask_list):
        pass









