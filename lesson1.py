summ=0
necessity_envelop=0
freedon_envelop=0
education_envelop=0
longterm_enbelop=0
play_envelop=0
gift_envelop=0

limit=1000
nec_rate = 0.55
ffa_rate = 0.1
edu_rate = 0.1
ltss_rate = 0.1
play_rate = 0.1
gift_rate = 0.05
print ("""Hello.
We're gonna fill your envelops by the money you input here!
Please input your amounts of money income and see the results.
Press Ctrl+c to exit script.
\n""")
while summ<=limit:
    income=float(input('Enter the amount please: '))
    summ+=income
    necessity_envelop+=income*nec_rate
    freedon_envelop+=income*ffa_rate
    education_envelop+=income*edu_rate
    longterm_enbelop=income*ltss_rate
    play_envelop+=income*play_rate
    gift_envelop+=income*gift_rate
print(f"""\nНаші гроші сумою {summ} розподілено наступним чином:
необхідні витрати: {round(necessity_envelop,2)}
фінансова свобода: {round(freedon_envelop,2)}
освіта {round(education_envelop,2)}
резерв та на великі покупки{round(longterm_enbelop,2)}
розваги {round(play_envelop,2)}
подарунки: {round(gift_envelop,2)}""")
        
    