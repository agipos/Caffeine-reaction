# Caffeine-reaction

The code below shows the outcome of an analysis done for a learning expirement. Participants were under the influence of caffeine, at 400g, 200g and no caffeine as a control, and then their reaction times were measured using a basic visual stimulus. 

Data was transferred from a .mat file into Python and recast into a workable type. Stimulus times were jittered in order for participants to be unable to anticipate when to react. Therefore, calculating the reaction times meant taking the total reaction time minus the stimulus onset. Some data was invalid due to participants "jumping the gun" and reacting before the stimulus presented. These values are presented as negative numbers and were removed from the data set, giving us the total valid trials.

All data in the valid trials was then plotted using matplotlib. 

![caffeinegraph](https://cloud.githubusercontent.com/assets/16911301/22131580/3c24dc4c-de69-11e6-93b0-d91300dfc315.png)
