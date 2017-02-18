"""
Bar chart demo with pairs of bars grouped for easy comparison.
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib

pp = PdfPages('ndlog_figs/standalone-vs-single-vs-clone-pct.pdf')

n_groups = 13

dedos = (98.957161,491.894714,982.561035,1471.610596,1959.748779,2448.988037,2546.994141,2582.265625,2564.070801,2557.179199,2530.352783,2437.254883,2484.694336)
perc_dedos = (1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 0.76, 0.74, 0.58, 0.52)

standalone = (99.516159, 492.111298, 980.828491, 1471.841797, 1961.140991, 2455.570312, 2767.424805, 2674.926025, 2704.820312, 2431.028076, 2515.553711,2514.72998, 2295.269531)
perc_standalone = (1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 0.94, 0.78, 0.69, 0.60, 0.56, 0.51, 0.50)

clone = (99.050098, 491.621338, 982.273407, 1472.41272, 1961.856323, 2451.741333, 2942.209595, 3432.860718, 3922.980347, 4409.141357, 4548.358643, 4761.921387, 4732.260742)
perc_clone = (1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 0.9992)



fig, ax1 = plt.subplots()

index = np.arange(n_groups)
bar_width = 0.25

opacity = 0.4
# error_config = {'ecolor': '0.3'}

rects1 = ax1.bar(index - bar_width, standalone, bar_width,
                 alpha=opacity,
                 color='b',
                 label='Standalone')

rects2 = ax1.bar(index, dedos, bar_width,
                alpha=opacity,
                color='g',
                label='DeDoS-Single')

rects3 = ax1.bar(index + bar_width, clone, bar_width,
                 alpha=opacity,
                 color='r',
                 label='DeDoS-Clone')

ax1.set_xlabel('Number of clients')
ax1.set_ylabel('Throughput (pkt/s)')
# plt.title('standalone vs dedos vs clone')
plt.xticks(index+ bar_width / 2, ('1', '5', '10', '15', '20', '25', '30', '35', '40', '45', '50', '55', '60'))
# plt.xticks(index + bar_width / 2, (l for l in labels))
plt.legend(loc=4)

ax2 = ax1.twinx()
ax2.plot(index + bar_width / 2, perc_standalone, color='b', alpha=opacity,  marker='.')
ax2.plot(index + bar_width / 2, perc_dedos, color='g', alpha=opacity,  marker='.')
ax2.plot(index + bar_width / 2, perc_clone, color='r', alpha=opacity,  marker='.')
ax2.set_ylabel('percentage received')
ax2.set_ylim([0,1.01])

matplotlib.rcParams.update({'font.size': 16})
plt.tight_layout()
# plt.show()
pp.savefig()
plt.close()
pp.close()
