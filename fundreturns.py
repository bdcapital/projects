#!/usr/bin/env python

#SACrets = {.25:.35,.5:.15,-.2:.1,.35:.3,.65:.25}
returnstates = [-.10,.00,.05,.20,.30]
probs =        [ .05,.05,.05,.60,.25]

cap = 10000000000
totalfee = .02 #.02 and .20 means 2 and 20 for these
returnfee = .20 

inputrets = dict(zip(returnstates,probs))

print "\n\n"
print "Return states"
print returnstates
print "Probabilities"
print probs
print "All probabilities sum to one? {}".format(True if sum(probs)==1.0 else str(False)) # Probabilities sum to one?
print "\n"

print "\nWith ${:,} under management, charging {} and {}, the fund is expected \
to perform as follows in a single year...".format(cap, totalfee*100, returnfee*100)


def hedgefundrets(capital=cap, returnprobs=inputrets, totfee=totalfee, retfee=returnfee):
	invgains = []
	fundgains = []
	rets = sorted(returnprobs.keys())
	for ret in rets:
		investors = capital
		stevie = 0
		# IF WE LOST MONEY
		if ret <= 0:
			stevie += totfee*capital #stevie makes money
			investors -= totfee*capital #you pay stevie
			investors *= 1+ret #you take hit
			invgains.append(investors*returnprobs[ret])
			fundgains.append(stevie*returnprobs[ret])
		# IF WE MADE MONEY
		elif ret > 0:
			stevie += totfee*capital #stevie gets his 2 on principal
			stevie += retfee*ret*capital #stevie gets his 20 on rets
			investors -= totfee*capital #investors pay stevie his 2
			investors *= 1+ret*(1-retfee) #investors make their return
			fundgains.append(stevie*returnprobs[ret])
			invgains.append(investors*returnprobs[ret])
	#print "invgains", invgains
	print "avg INVESTOR return: %", (sum(invgains)-capital)/capital*100
	print "avg FUND revenue: {:,}".format(sum(fundgains))
	return sum(fundgains)

hedgefundrets()


