import threading
import random
import time

MAX_COORDINATE_VALUE = 50
NUMBER_OF_THREADS = 12

cutsArr = []
k_coof = []
results = []




class MyThread(threading.Thread):
    period = []
    def __init__(self, period):
        self.period = period
        threading.Thread.__init__(self)

    def run ( self ):
        for i in range(self.period[0],self.period[1]):
            self.find_same(i)

    def find_same(self,index):
        count = 1
        for x in k_coof[index+1:]:
            if(k_coof[index]==x):
                #remove to see the results#####################################
                #print("paralel: "+str(index)+" - "+str(index+count))
                results.append([index,index+count])
            count+=1





def rand():
    return int(random.uniform(-MAX_COORDINATE_VALUE,MAX_COORDINATE_VALUE))

def createCuts(n):
    for i in range(n):
        #[x1,y1,x2,y2]
        cutsArr.append([rand(),rand(),rand(),rand()])
        while((cutsArr[-1][2]-cutsArr[-1][0])==0):
            cutsArr[-1] = [rand(),rand(),rand(),rand()]

        k_coof.append((cutsArr[-1][3]-cutsArr[-1][1])/(cutsArr[-1][2]-cutsArr[-1][0]))
        #remove to see the results#####################################
        #print(str(i)+": coordinates: "+str(cutsArr[-1])+ "; k cooficient = "+str(k_coof[-1]))
    return cutsArr


def executeThreads(numb_of_threads,n):
    c = int(n/numb_of_threads)
    #print("c = " + str(c))
    th = []
    for i in range(numb_of_threads):
        #print("-----"+str(i*c)+"======"+str((i+1)*c)+"------")
        th.append(MyThread([i*c,(i+1)*c]))
        th[-1].start()
    for t in th:
        t.join()

def find_same_iterable(n):
    for i in range(n):
        for x in range(i+1,n):
            if(k_coof[i] == k_coof[x]):
                #remove to see the results#####################################
                #print("iter: "+str(i)+" - "+str(x))
                results.append([i,x])



def main():
    global results
    print("Enter number of cuts to generate")
    n = int(input())
    createCuts(n)
#--------------------------------------------------------------------
    time_start = time.time()

    executeThreads(NUMBER_OF_THREADS,n)
    #for i in range(n):
    #    MyThread(i).start()

    end_time = time.time()
    #print(str(results))
    print("Threads TIME SPENT: "+ str(end_time-time_start)+" seconds")
#---------------------------------------------------------------------
    results = []
    time_start = time.time()

    find_same_iterable(n)

    end_time = time.time()
    #print(str(results))
    print("Iterable TIME SPENT: "+ str(end_time-time_start)+" seconds")
#----------------------------------------------------------------------




if __name__ == "__main__":
    main()
