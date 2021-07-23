
import sys
sys.path.append('../')
from pycore.tikzeng import *
from pycore.blocks  import *

arch = [ 
    to_head('..'), 
    to_cor(),
    to_begin(),
    
    #input
    to_input( '../examples/YOLO/left2159.jpg', width=12, height=9),
    to_Conv("conv1", 640, 16, offset="(0,0,0)", to="(0,0,0)", height=48, depth=64, width=2 ),
    to_Pool("pool1", offset="(0,0,0)", to="(conv1-east)", height=24, depth=32),
    to_connection( "pool1", "conv2"), 
    to_Conv("conv2", 320, 32, offset="(0,0,0)", to="(0,0,0)", height=24, depth=32, width=2 ),
    to_Pool("pool2", offset="(0,0,0)", to="(conv1-east)", height=12, depth=16),
    to_end() 
    ]


def main():
    namefile = str(sys.argv[0]).split('.')[0]
    to_generate(arch, namefile + '.tex' )

if __name__ == '__main__':
    main()
    
