#date of birth 03/29/1996

# #import dependencies
from mrjob.job import MRJob
#Create a class called HP_count, which inherits, or takes properties, from the MRJob class.
class HP_Count(MRJob):
#creating a mapper()function that assigns the input to key -value pairs  
                    def mapper(self, _, line):
                          for word in line.split():
                                   yield(word, 1)
                
#creating a reducer()function               
                    def reducer(self, word, counts):
                          yield(word, sum(counts))
#python code for running the program                         
if __name__ == '__main__':
         HP_Count.run()