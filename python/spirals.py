import sympy
import numpy as np
import matplotlib.pyplot as plt

CARDINAL_RED       = (0.55, 0.08, 0.08)
CARDINAL_SANDSTONE = (0.82, 0.76, 0.58)

N=[5000, 10000, 50000]



fig, ax = plt.subplots(figsize=(160, 90), nrows=1, ncols=len(N), subplot_kw=dict(projection='polar'), facecolor=CARDINAL_SANDSTONE)


for i, thisN in enumerate(N):

    # Avoids 'object is not subscriptable' TypeError if len(N)=1
    if len(N)>1:
        thisAx=ax[i]
    else:
        thisAx=ax

    p = np.asarray(list(sympy.primerange(0, thisN)))

    # Plots
    thisAx.plot(p, p,'ro', markersize=0.5, color=CARDINAL_RED)


    for r_label in thisAx.get_yticklabels():
        r_label.set_text('')

    thisAx.set_ylim(0,np.max(p))
    thisAx.grid(False)
    thisAx.set_xticklabels([])
    thisAx.set_yticklabels([])
    thisAx.axis('off')
    thisAx.set_title('N=%d' % thisN, color=CARDINAL_RED, fontweight='extra bold', fontsize=30, fontstyle='italic')

fig.suptitle('Prime Numbers spirals', color=CARDINAL_RED, fontweight='extra bold', fontsize=60)
plt.figtext(0.5, 0.15, 'https://github.com/pietro-caragiulo/spirals', ha='center', va='center', color='gray', fontstyle='italic')

plt.show()

fig.savefig('spirals.png', facecolor=CARDINAL_SANDSTONE)
