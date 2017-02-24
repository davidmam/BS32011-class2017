filename= input('which file to oneline?')

open(filename+'.one.txt', 'w').write(''.join(open(filename).read().split('\n')[1:]))

