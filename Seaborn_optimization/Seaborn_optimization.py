ax.legend(fontsize=12, loc='upper left') # legend position

plt.title('Scatter Plot of iris by matplotlib', fontsize=20)

plt.xlabel('Petal Length', fontsize=14)

plt.ylabel('Petal Width', fontsize=14)


sns.set(font_scale=1.5)

plt.legend(loc='upper left', bbox_to_anchor=(1.0, 1.0))

plt.xlim(0, 50000)

plt.xticks(rotation = - 45 )

plt.tight_layout()
plt.show()

ax.set_xticklabels(ax.get_xticklabels(),rotation=45,ha="right",rotation_mode='anchor')
plt.tight_layout()


plt.xlim(left, right)
plt.ylim(bottom, top)

plt.xscale('log')
plt.xscale('linear')
plt.xscale('logit')
plt.xcale('symlog')

plt.xticks(np.arange(min(x), max(x)+1, 1.0))


plt.xscale('log')


# Definition of tick_val and tick_lab
tick_val = [1000,10000,100000]
tick_lab = ['1k','10k','100k']

# Adapt the ticks on the x-axis
plt.xticks(tick_val,tick_lab)

# You can see all possible shapes:
all_shapes=markers.MarkerStyle.markers.keys()
all_shapes
#[0, 1, 2, 3, 4, u'D', 6, 7, 8, u's', u'|', 11, u'None', u'P', 9, u'x', u'X', 5, u'_', u'^', u' ', None, u'd', u'h', u'+', u'*', u',', u'o', u'.', u'1', u'p', u'3', u'2', u'4', u'H', u'v', u'', u'8', 10, u'&lt;', u'&gt;']

