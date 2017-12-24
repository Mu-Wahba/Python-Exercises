import os
import argparse


parser=argparse.ArgumentParser(description="Check if the file exists")
parser.add_argument("-F","--file",metavar='',type=str,help='file name',required=True)
parser.add_argument("-P","--path",metavar='',type=str,help='path name')
args=parser.parse_args()



if args.path:
    if(any(f == args.file for f in os.listdir(args.path))):
        print(os.stat(os.path.join(args.path,args.file)))    
else:
    if(any(f == args.file for f in os.listdir(os.getcwd()))):
        print(os.stat(os.path.join(os.getcwd(),args.file)))
