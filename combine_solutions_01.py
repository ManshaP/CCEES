import requests
import json

nb_name = 'solution_01' + '.ipynb'

nb_urls = [
'https://raw.githubusercontent.com/ManshaP/CCEES/master/exercise_1/1_pedestrian\'s_solution_of_ODE_system.ipynb',
'https://raw.githubusercontent.com/ManshaP/CCEES/master/exercise_1/2_glycolysis_model.ipynb',
'https://raw.githubusercontent.com/ManshaP/CCEES/master/exercise_1/4_saddle_node_bifurcation.ipynb',
'https://raw.githubusercontent.com/ManshaP/CCEES/master/exercise_1/5_globally_stable_subcritical_pitchfork_bifurcation.ipynb'
]

combined_dict = {
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": nb_name,
      "version": "0.3.2",
      "provenance": []
    },
    "language_info": {
      "codemirror_mode": {
        "name": "ipython",
        "version": 3
      },
      "file_extension": ".py",
      "mimetype": "text/x-python",
      "name": "python",
      "nbconvert_exporter": "python",
      "pygments_lexer": "ipython3",
      "version": "3.7.3"
    },
    "kernelspec": {
      "display_name": "Python 3",
      "language": "python",
      "name": "python3"
    }
  }
}

cells = []

for nb_url in nb_urls:
    r = requests.get(nb_url)
    content = json.loads(r.text)

    for cell in content['cells']:
        cells.append(cell)

combined_dict['cells'] = cells

with open(nb_name, 'w') as outfile:
    json.dump(combined_dict, outfile)
