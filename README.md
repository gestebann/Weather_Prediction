Weather prediction project

#I am plannning to use linear regression method to predict the minimum temperature on a day by giving the maximum temperature of that day.
#I will be using python.
#I'm planning to use the method in this project on other predictions as well.
#I will be using csv data format.

25.01.20 - I've found a dataset which includes temperature values of a city in north carolina, USA. resource:(data.gov)
         - Downloaded the required libraries -> (sklearn, numpy, pandas, seaborn, matplotlib)
         - I was able to get a table view of my dataset and some quantities as well.
         - I drew some plots to understand if my dataset is suitable to work with linear regression.(it is)
         - Splitted data (%20 test - %80 train)
         - Trained and tested. And checked accuracy. mean absolute error was around 5.
         - final
         - After predicting temperature ı tried to predict other values such as rain precipitation, windspeed etc.
         - It didn't work out well. I think its because the weather was so hot and there were few days that rains.
      
Conclusions..Linear regression is useful but in some certain situations. Because it just draws a linear line and doesn't flex.
            .For example when I was  trying to predict if the day was rainy or not, in most cases temperature was hot and it wasnt raining but 
            if temperature goes lower than a specific level usually it rains. And the problem is the linear regression algorithm doesnt care 
            about exceptations like this.
            .I will try to predict rain precipitation by using another method.
            

;ibrahim aslan
