YOLO project

Model darknet yolov3 416

directories:

1. Code:
        
       project/vehicle_and_person_detection/code
       

       for image :
                   file: yolo_image.py

                   command: python yolo_image.py 

                   for save the detected image: python yolo_image.py --save True
                  
                   Dependent folder: code/input:- handlabel(40 images) , coco(validation2017) specific to vehicle and person

                   Takes images from handlabel_images or coco_validation_images 
                   save detected bounding box text files handlabel_detected-results or coco_detected-results
                   save detected images detected-images

       for video : 
                   file: yolo_video.py
 
                   command: python yolo_output.py --input <file-name> --output 
       
                   for save the text (detected bounding) file separately python yolo_output.py --input <file-name> --output --save_file_separately

                   for save the text (detected bounding) file python yolo_output.py --input <file-name> --output --save_file

                   video save in out_video folder
                   input video path : video (todo) presently code
      
       for mAP :
                  file: calculate_map.py
                 
                  command: python calculate_map.py

                  folder requirement: coco_ground-truth, coco_detected-results , coco_validation_images(optional)
                  result: results/<filename>

train : 

     file : train.py
     
     command: pthon train.py

     Note: change weights, anchor and classes path in train.py as per the need
      
     


                  

