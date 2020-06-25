#Mybench.py
from m5.objects import Process

# You should change these variables #

#Binary path for spec2006 binary
binary_dir = '/home/nobleminsu/calab_selection/SPECCPU2006_binary/'
#Data path for spec2006
data_dir = '/home/nobleminsu/calab_selection/SPECCPU2006_input/'


#401.bzip2
bzip2 = Process()
bzip2.executable =  binary_dir+'bzip2/bzip2'
data=binary_dir+'bzip2/input.program'
bzip2.cmd = [bzip2.executable] + [data, '1']
bzip2.output = 'input.program.out'


#429.mcf
mcf = Process()
mcf.executable =  binary_dir+'mcf/mcf'
data=data_dir+'429.mcf/data/test/input/inp.in'
mcf.cmd = [mcf.executable] + [data]
mcf.output = 'inp.out'

#450.soplex
soplex=Process()
soplex.executable =  binary_dir+'soplex/soplex'
data=data_dir+'450.soplex/data/test/input/test.mps'
soplex.cmd = [soplex.executable]+['-m10000',data]
soplex.output = 'test.out'

#456.hmmer
hmmer=Process()
hmmer.executable =  binary_dir+'hmmer/hmmer'
data=data_dir+'456.hmmer/data/test/input/bombesin.hmm'
hmmer.cmd = [hmmer.executable]+['--fixed', '0', '--mean', '325', '--num', '5000', '--sd', '200', '--seed', '0', data]
hmmer.output = 'bombesin.out'

#458.sjeng
sjeng=Process()
sjeng.executable =  binary_dir+'sjeng/sjeng'
data=data_dir+'458.sjeng/data/test/input/test.txt'
sjeng.cmd = [sjeng.executable]+[data]
sjeng.output = 'test.out'
#462.libquantum
libquantum=Process()
libquantum.executable =  binary_dir+'libquantum/libquantum'
libquantum.cmd = [libquantum.executable],'33','5'
libquantum.output = 'test.out'

#470.lbm
lbm=Process()
lbm.executable =  binary_dir+'lbm/lbm'
data=data_dir+'470.lbm/data/test/input/100_100_130_cf_a.of'
lbm.cmd = [lbm.executable]+['20', 'reference.dat', '0', '1' ,data]
lbm.output = 'lbm.out'

