# Régulation de la tension

### Pourquoi réguler la tension ?

La tension livrée aux consommateurs doit rester proche de sa valeur nominale (20 kV). Trop basse, les moteurs chauffent et les appareils s'arrêtent ; trop haute, le matériel s'abîme. Or elle baisse naturellement quand la charge augmente. Les consommateurs demandent plus de puissance (P = U × I) et, la tension étant à peu près imposée, c'est le courant I qui augmente. Ce courant traverse la résistance R du réseau, qui est fixe, et y provoque une chute de tension R × I. La tension qui reste pour les consommateurs, U_source − R × I, est donc d'autant plus basse que le courant est élevé (le soir, en hiver avec le chauffage) : à prise fixe, elle perd environ 1 kV entre une nuit d'été et un soir d'hiver. On régule donc en changeant la prise du transformateur (environ 0,25 kV par prise) : on la monte quand la tension est trop basse, on la descend quand elle est trop haute.

## Modèle de simulation de la tension
La tension de sortie U_HTA ne dépend pas directement du jour : 
Elle découle d’une chaîne de calcul. L’heure fait varier la charge et la tension du réseau (courbe type de la journée P(h), avec un creux la nuit et une pointe le soir).
Le jour fait varier la charge selon la saison S(jour)
Cette variation est représentée par un facteur allant de 0 à 1 : plus ce facteur est élevé, plus il y a de charge sur le réseau. Par exemple, en hiver, le facteur est maximal (1) : le chauffage électrique fait monter la consommation, la charge est élevée et la tension baisse davantage. En été, le facteur est plus faible (0,6) : la charge est environ 40 % plus basse et la chute de tension est moins marquée.

. La prise du régleur ajuste le rapport de transformation (1,25 % par prise, 0,25 kV environ). 

Le modèle complet ajoute deux petits aléas lents, qui rendent chaque journée différente :


I_charge = 950 × P(h) × S(jour)          (A)
U_HTB    = 64 − 2 × P(h)                 (kV)
U_HTA    = 20 × (U_HTB / 63) × (1 + 0,0125 × (prise − 9)) − 0,001 × I_charge     (kV)


Pour démarrer, on simplifie : plus d’aléas, saison figée en hiver (S = 1), tension amont fixée à 63 kV, et courbe de journée réduite à 4 points (4 h : 0,45 ; 9 h : 0,85 ; 19 h : 1,00). Il ne reste que l’heure et la prise comme variables, et l’écart avec le modèle complet reste inférieur à une prise (de −0,12 à +0,32 kV sur la journée). Cette version garde l’essentiel : la tension baisse quand la charge monte, et il faut remonter la prise pour compenser.

I_charge = 950 × P4(h)                                                (A)
U_HTA    = 20 × (1 + 0,0125 × (prise − 9)) − 0,001 × I_charge         (kV)
