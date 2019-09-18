TouchDetector.loop should be run every with every data sample.
Test.py contains basic test cases, run it to run them

If you wanted to add other motions, you could just add more motion classes with different "detect" methods.
If you had training data for other motions you might want to define them in a more generic way. I think if you went down
this route you would want to divide the data up into distinct motions (So from the beginning to the end of contact is
one motion).

Once you had done this you could chunk up the data a bunch so each motion was like 3-4 total timesteps (the approximate
maximum different states for any currently defined motion). At this point, any possible motion is definable by the same
set of rules, like a hit is " hard touch on one or more adjacent sensors for a short duration and then release". Your
new motions would presumably be able to be put into this mold by hand, or if you were particularly bold you could use
ML. I think you would want to use a neural net because your features are closely intertwined. I don't forsee many
situations in which this is easier than manually figuring out what criteria make up the motion.