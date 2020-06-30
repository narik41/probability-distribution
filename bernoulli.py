import math 

class Bernoulli:

    """ 
        Bernoulli class  for calculating and visualizing the bernoulli distribution

        Attributes:
            p(float) - represeting the probability of event occuring
    """
    def __init__(self, p):
        self.p = p 
        self.n = 1 
    
    def calculate_mean(self):
        """ 
            Function to calculate the mean from p 

            Returns : 
                float : mean of the data 

        """
        return self.p

    def calculate_variance(self):
        """ 
            Function to calculate the variable of data 

            Returns :
                float : variance of the data
        """ 

        return self.p(1- self.p)

    def calculate_stdev(self):
        """
            Function to calculate the standard distribution of data 

            Returns:
                float : stdev of the data
        """
        return math.sqrt(self.calculate_variance)

    def pdf(self, k):
        """ 
            Probability density function calculator for bernoulli distribution 

            Args : 
                k(float) : point for calculating the pdf 

            Returns : 
                float : pdf at point k 
        """
        return (self.p ** k ) * (1- self.p)**(1-k)

    

    