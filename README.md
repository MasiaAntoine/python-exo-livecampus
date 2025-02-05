## Prérequis ⚙️

Assurez-vous d'avoir un environnement virtuel configuré. Pour activer l'environnement virtuel, exécutez les commandes suivantes :

```bash
/opt/homebrew/opt/python@3.11/bin/python3.11 -m venv /Users/antoine/Projet/python-exo-livecampus/venv
source /Users/antoine/Projet/python-exo-livecampus/venv/bin/activate
```

## Utilisation 🚀

### Exécution des scripts 📜

Pour exécuter les scripts `main.py`, utilisez les commandes suivantes :

```bash
python3.11 /Users/antoine/Projet/python-exo-livecampus/exo1/main.py
python3.11 /Users/antoine/Projet/python-exo-livecampus/exo2/main.py
python3.11 /Users/antoine/Projet/python-exo-livecampus/exo3/main.py
python3.11 /Users/antoine/Projet/python-exo-livecampus/exo4/main.py
python3.11 /Users/antoine/Projet/python-exo-livecampus/exo5/main.py
```

### Exécution des tests 🧪

Pour exécuter les tests, utilisez les commandes suivantes :

```bash
cd /Users/antoine/Projet/python-exo-livecampus/exo6/
python -m unittest discover
pytest test_deck_pytest.py
```

### Démarrage de FastAPI ⚡

Pour démarrer FastAPI, utilisez la commande suivante :

```bash
cd /Users/antoine/Projet/python-exo-livecampus/exo7 && uvicorn main:app --reload
```

### Démarrage de SQLite 🗄️

Pour démarrer SQLite, utilisez la commande suivante :

```bash
cd /Users/antoine/Projet/python-exo-livecampus/exo8 && uvicorn main:app --reload
```
