import pandas as pd
import matplotlib.pyplot as plt

class calUtils:
        def visit(self):
                dict = {"country": [" United Kingdom "," Germany "," France "," Italy "," Netherlands "," Greece "," Belgium & Luxembourg "," Switzerland "," Austria "," Scandinavia "," CIS & Eastern Europe "],
                        "num": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
                        "sums": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]}

                df = pd.DataFrame(dict, columns=['country', 'num', 'sums'])
                dff = pd.read_csv('IMVA.csv')

                uk = dff[' United Kingdom '].sum()
                ger = dff[' Germany '].sum()
                fra = dff[' France '].sum()
                ita = dff[' Italy '].sum()
                net = dff[" Netherlands "].sum()
                gre = dff[" Greece "].sum()
                bel = dff[" Belgium & Luxembourg "].sum()
                swi = dff[" Switzerland "].sum()
                aus = dff[" Austria "].sum()
                sca = dff[" Scandinavia "].sum()
                cns = dff[" CIS & Eastern Europe "].sum()

                df['sums'] = df['sums'].replace(1,uk)
                df['sums'] = df['sums'].replace(2,ger)
                df['sums'] = df['sums'].replace(3,fra)
                df['sums'] = df['sums'].replace(4,ita)
                df['sums'] = df['sums'].replace(5,net)
                df['sums'] = df['sums'].replace(6,gre)
                df['sums'] = df['sums'].replace(7,bel)
                df['sums'] = df['sums'].replace(8,swi)
                df['sums'] = df['sums'].replace(9,aus)
                df['sums'] = df['sums'].replace(10,sca)
                df['sums'] = df['sums'].replace(11,cns)

                df.sort_values(by=['sums'], inplace=True, ascending=False)
                df.reset_index(drop=True, inplace=True)

                newdf = df.nlargest(3,'sums')
                print(newdf)
                df['countries'] = df['country']
                df.index = df["country"]
                del df["num"]
                del df["country"]
                print(df)
                #Top 3 bar chart
                ax = newdf.plot(kind='bar', x='country', y='sums', title="Number of Visitors in Countries",
                        ylabel="Number of Tourists (in millions) ", rot=0, legend=False, figsize=(15, 15))
                for p in ax.patches:
                        ax.annotate(str(p.get_height()), (p.get_x() * 1.005, p.get_height() * 1.005))
                plt.savefig("scatterDiagram_Top3.png")
                #plt.show()

                # all countries bar chart
                ax = df.plot(kind='bar',x='countries',y='sums',title="Number of Visitors in Countries",
                        ylabel="Number of Tourists (in millions) ",rot=45, legend=False, figsize=(25,25))
                for p in ax.patches:
                        ax.annotate(str(p.get_height()), (p.get_x() * 1.005, p.get_height() * 1.005))
                plt.savefig("Country_comparison.png")
                #plt.show()


j = calUtils()
print(j.visit())
