## Prérequis

Assurez-vous d'avoir un environnement virtuel configuré. Pour activer l'environnement virtuel, exécutez les commandes suivantes :

```bash
/opt/homebrew/opt/python@3.11/bin/python3.11 -m venv /Users/antoine/Projet/python-exo-livecampus/venv
```

```bash
source /Users/antoine/Projet/python-exo-livecampus/venv/bin/activate
```

## Utilisation

Pour exécuter les scripts `main.py`, utilisez la commande suivante :

```bash
python3.11 /Users/antoine/Projet/python-exo-livecampus/exo1/main.py
```

```bash
python3.11 /Users/antoine/Projet/python-exo-livecampus/exo2/main.py
```

```bash
python3.11 /Users/antoine/Projet/python-exo-livecampus/exo3/main.py
```

```bash
python3.11 /Users/antoine/Projet/python-exo-livecampus/exo4/main.py
```

```bash
python3.11 /Users/antoine/Projet/python-exo-livecampus/exo5/main.py
```

Pour executer les tests, utilisez la commande suivante :

```bash
cd /Users/antoine/Projet/python-exo-livecampus/exo6/
python -m unittest discover
```

```bash
pytest test_deck_pytest.py
```

Pour démarrer fastapi :

```bash
cd /Users/antoine/Projet/python-exo-livecampus/exo7 && uvicorn main:app --reload
```
