import cv2
import os
import re
from argparse import ArgumentParser

parser = ArgumentParser(description="",usage='use "python3 %(prog)s --help" for more information')
# the recourse path
parser.add_argument('--input_path','-input')
# the output path
parser.add_argument('--output_path','-out')
# the log path
parser.add_argument('--log_path','-log')
args = parser.parse_args()

in_path= args.input_path
out_path = args.output_path
log_path = args.log_path

all_file_resource = [i for i in os.listdir(in_path) if '.mp4' in i]

# log the frame number
f = open(log_path,'w')

count = 0
for i in sorted(all_file_resource, key = lambda x: int(''.join([i for i in re.findall(r'^sp\d+_',x)[0] if i.isdigit()]))):
    print(i)
    real_path = in_path + '/' + i
    vidcap = cv2.VideoCapture(real_path)
    success,image = vidcap.read()
    output_path = out_path + '_' + i
    while success:
        cv2.imwrite(os.path.join(output_path,"frame%d.png" % count), image)     # save frame as JPEG file 
        f.write('count: ' + str(count) + '\n')
        success,image = vidcap.read() 
        print('Read a new frame: ', success)
        count +=1
        
        
f.close()


    
