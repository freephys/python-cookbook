m1 = Measurement(100.0, 5.5)   # measured value of 100.0 with 5.5% error
m2 = Measurement(50, 2)        # measured value of 50.0 with 2% error
print "m1 = ", m1
print "m2 = ", m2
print "m1 + m2 = ", m1 + m2
print "m1 - m2 = ", m1 - m2
print "m1 * m2 = ", m1 * m2
print "m1 / m2 = ", m1 / m2
print "(m1+m2) * (m1-m2) = ", (m1+m2) * (m1-m2)
print "(m1-m2) / (m1+m2) = ", (m1-m2) / (m1+m2)
# emits:
# m1 =  100+-5.5%
# m2 =  50+-2%
# m1 + m2 =  150+-3.72678%
# m1 - m2 =  50+-11.1803%
# m1 * m2 =  5000+-5.85235%
# m1 / m2 =  2+-5.85235%
# (m1+m2) * (m1-m2) =  7500+-11.7851%
# (m1-m2) / (m1+m2) =  0.333333+-11.7851%
