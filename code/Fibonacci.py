class Fibonacci() :
    '''
     * Class containing a method to compute the Fibonacci sequence
     *
     *
     * @author José Blázquez
     */
     '''
    YoungRabbit = 0;
    OldRabbit = 1;
    Result = 1;

    def init_(self):
        pass

    def compute(self,  numbermonth, pair):
        if (numbermonth < 0) :
            raise Exception("The value is negative: " + numbermonth);
        elif numbermonth==1 or numbermonth==2:
            Result=1;
        else:
            for generation in range(1, numbermonth):
                result = YoungRabbit + OldRabbit;
                YoungRabbit = OldRabbit*pair;
                OldRabbit = result;
                generation+=1;

            return result;
