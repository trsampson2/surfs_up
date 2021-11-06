# Surfs_up Weather Analysis

## Overview of statistical analysis
 
The owner of Surfs Up, a surf and ice cream shop business, is evaluating whether he should open up a shop in Oahu based on the weather throughout the year.  Good weather promises that the business will be sustainable year round. W. Avy wants more information about temperature trend.  This study uses SQLAlchemy to query the data and create Pandas DataFrames to gain statisical analysis. 

## Results
The key differences of weather between the months of June and December
- The mean tempearture is approximately 75 degrees in June and 71 degrees in December. 
- The minimum temperature is 64 degrees in June and 56 degrees in December.
- The range of temperature is 21 degrees in June and 27 degrees in December. 

![June_temps_stat](https://user-images.githubusercontent.com/86331812/140621520-55e7a211-2fea-4438-b442-e8c0aa187218.png)
June Temperature Statistics


![Dec_temps_stat](https://user-images.githubusercontent.com/86331812/140621527-f0fc6f30-615d-483b-9bf1-d500854631cb.png)
December Temperature Statistics


## Summary
This study shows that there are differences in weather in the months of June and December. Look at at the statistical analysis shows there is a slight difference in the mean of the temperatures, but the range shows that the temperature in December can lower to a point where ice cream or surfing is not desireable. Before determining if it was a surf and ice cream shop would be a good business decision, additional queries are needed.  I would write a query to look at how many days each temperature occurs.  If it is known how many days there is suboptimal tempertures, a better decision can be made about whether or not to open a shop in Oahu.  I would also look at the location of stations to see where the optimal location would be in Oahu. This would help to pinpoint the locations. 
