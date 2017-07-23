VPN Anonymity Threat Modeling Gist



VPNs, Anonymity, and Threat Modeling

VPNs --> Anonymity --> Threat Modeling


VPNs

	What is a VPN?
		Virtual Private Network. 
			Analogy: 
				Castle with outside tunnel leading to another castle, fully enclosed by stone, doesn't allow others to see in, is heavily defensible, but can be destroyed given powerful enough weaoponry, or knowledge of architecture.

		Network laid on top of another. 
			Exists "logically/virtually", not physical.
		No guarantee of encryption*

	Kinds of VPNs:
		Gateway
		Tunnel
		Uses of each
			Tunnel - point to point (funnel)
			Gateway -> inverse funnel
	
		What do VPNs protect against?
			MiTM spying over insecure network segments.
			True Source/Destination hiding against non-global/infrastructure controlling adversaries.
			Per-application/protocol throttling*

	Can VPNs be defeated?
		Yes:
			Password bruteforcing, 
			Implementation flaws(cryptograghic related), 
			Key theft
	
	What should one be mindful of while using a VPN?
		Why am I using a VPN? 
			For what purpose?
				Does usage of a VPN help me in my threat model?

		A VPN does not give full anonymity or privacy. It can prevent a website from knowing your IP location, and keep local network users from knowing your penultimate destinations, however, VPN traffic is easily identifiable amongst general internet traffic(VPN link). If your adversary has a global presence, and they are able to monitor entrance/exit locations, they can perform correlative analysis. 

		A VPN will not protect you legally.*
			If you commit crimes using a VPN to mask your traffic origination, LE  *will* go knocking on that service providers door. Do you think they're *not* going to give the police all their logs? Things like Mutual Legal Assistance Treaties(MLATs) exist. So, just because you hop through Russia, doesn't mean you won't have LE successfully find you. 

		A VPN does not guarantee anonymity.
			This should never be assumed. At best it is obfuscation, at worst it is a form of identification


	That being said, 

		Should one be using a VPN as a default action?
			Most always* 
				*personal opinion


Threat model for the VPN usage model(you’re not stopping the NSA/GCHIQ/BND), you are stopping coffee shop skiddies. You are creating a "secure" tunnel from point A <--> point B. Point A being your computer, point B being the VPN termination point(you have to access the internet somehow). This means your traffic leaves the VPN tunnel the same as it enters it, whether it is encrypted or not. 

Analogy: 
	Traveling by ship in international waters, from america to Hawaii. On the ship, you are protected by the ship, when you step off, you are no longer protected by the ship and instead must rely on what you have on your person. Ship = VPN tunnel, you = data packet.

	Where/what type of VPN service should be used?
		Depends on usage case/familiarity with technology
			78% of the time: [Algo](https://github.com/trailofbits/algo)
			22%: [OpenVPN](https://openvpn.net/howto.html)


Anonymity

	Anonymity: hiding your Identity

	Dictionary.com defines anonymity as: "lack of outstanding, individual, or unusual features; impersonality.
    "the anonymity of big city life definitely has its advantages"

    How can we achieve anonymity?
    	panopticlick
    	timing
    	correlation analysis


    Is it possible?
    	(Silence on the Wire - lcamtuf)

    Is it necessary?
    	How much?
    	Against whom?

    Limitations?

    Anonymity is hard. Really hard. Especially if you're already known. 

    Achieving anonymity is a subject of research deserving of its own. It is different for each individual, in that  specific context. The nail that sticks up gets hammered. It's hard to find a needle in a stack of them. 

See the "grugq's 'Hacker's Guide to Opsec". Learning about operational security and how it may help you achieve/maintain anonymity is also a topic deserving of its own time. I can only recommend that you look to the existing public bodies of knowledge put out by the proffessionals in the field(Intelligence agency declassified publications), Allen Dulles Guide to tradecraft as an example.

Tools that you can use to aid in achieving anonymity: TAILS, a VPN, Tor, a laptop with the hard drive ripped out, boots only from microsd/USB, yagi antennae, coffee shop wifi, etc.

In terms of easy 3 part scale:

1. Use nothing -> Everyone with eyes on the network sees all your communications. Identifying you is easy.

2. Using VPN/TOR -> Global passive adversary can perform correlative analysis on your traffic and id you that way. 

We can see that the cost of achieving higher and higher levels of anonymity ROI does not scale nicely in terms of energy/money. One must be sure of the desired level of anonymity is properly needed, vs wanted.



Threat Modeling

	OWASP on Threat Risk Modeling: https://www.owasp.org/index.php/Threat_Risk_Modeling
	Microsoft Threat Modeling Web Applications: https://msdn.microsoft.com/en-us/library/ff648006.aspx#tmwa_approach


	Different Types:
		[STRIDE](https://msdn.microsoft.com/en-us/library/ee823878(v=cs.20).aspx) - Microsoft creation - Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, and Elevation of Privilege
      
		[P.A.S.T.A (Process for Attack Simulation and Threat Analysis)](https://www.owasp.org/images/a/aa/AppSecEU2012_PASTA.pdf)
		
    [Trike](http://octotrike.org/) 
		
    [Octave](http://www.cert.org/resilience/products-services/octave/)
		
    [DREAD](https://en.wikipedia.org/wiki/DREAD_(risk_assessment_model)
		
    [VAST - Visual Agile Simple Threat](https://www.peerlyst.com/posts/introducing-the-visual-agile-and-simple-threat-modeling-methodology-vast-designed-for-scalability-brian-beyst-mba)
    Ad-Hoc

	We're going to touch on Ad-Hoc primarily, not really interested in the others, as this is in relation primarily to personal threats, not as an organization/software product.




