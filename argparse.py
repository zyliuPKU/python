import argparse
def parse_args():
  parser=argparse.ArgumentParser()
  parser.add_argument('-s',dest='sdate',default='')
  parser.add_argument('-e',dest='edate',default='')
  return parser.parse_args()
args=parse_args()
# args.sdate,args.edate
