session = Session()
# subs = session.query(SubTask,SubtaskProperty).filter(SubTask.status == 0).filter(SubTask.property.tag == 'ICT_ICT').all()


subs = session.query(SubTask).select_from(SubTask).join(SubtaskProperty,SubtaskProperty.subtask_name == SubTask.name).filter( SubTask.status == 0 ).filter(SubtaskProperty.tag == 'ICT_ICT').all()
for s in subs:
    print s.name
session.commit()
session.close()

default_benchmark = session.query(Benchmark).order_by(Benchmark.checkin_time.desc()).first()