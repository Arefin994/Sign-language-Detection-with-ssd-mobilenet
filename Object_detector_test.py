import object_detection
print("Worked: "+object_detection.__file__)


'''

you have to run --- 
$env:PYTHONPATH = "D:\models\research;D:\models\research\slim"
python scripts/generate_tfrecord.py -x "workspace/images/train" -l "workspace/annotations/label_map.pbtxt" -o "workspace/annotations/train.record"
python scripts/generate_tfrecord.py -x "workspace/images/test" -l "workspace/annotations/label_map.pbtxt" -o "workspace/annotations/test.record"

'''