# 🧪 Gestion des Fluides - Application Flask

Ce projet est une application de gestion des fluides médicaux utilisant **Flask** et une base de données **MySQL/MariaDB**.  
Elle permet de gérer les utilisateurs, les rôles et les enregistrements des fluides.

---

## ✅ Prérequis

Avant de commencer, assurez-vous d’avoir :

- **Python 3.x** → [Télécharger](https://www.python.org/downloads/)
- **MySQL** ou **MariaDB** (assurez-vous que le serveur tourne)

---

## ⚙️ Installation

### 1. Cloner et naviguer dans le dossier du projet

```bash
git clone https://github.com/nospi510/gestion-fluides.git
cd gestion-fluides
````

### 2. Créer un environnement virtuel

#### 💻 Sur **Windows** :

```bash
python -m venv venv
.\venv\Scripts\activate
```

#### 🐧 Sur **Ubuntu/Linux** :

```bash
python3 -m venv venv
source .venv/bin/activate
```

---

### 3. Installer les dépendances

```bash
pip install -r requirements.txt
```

---

### 4. Configuration de la base de données

* Connectez-vous à MySQL ou MariaDB :

```sql
CREATE DATABASE fluide_db;
```

* Modifiez les informations de connexion dans **`app/__init__.py`** :
  Remplacez l’utilisateur, le mot de passe et le nom de la base si besoin :

```python
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://<user>:<password>@localhost/fluide_db'
```

---

### 5. Lancer l'application Flask

```bash
python run.py
```

L'application sera accessible sur :
👉 [http://localhost:5001]

---

## 👤 Création d’un utilisateur administrateur

 ⚠️ Nécessaire pour se connecter la première fois.

Dans **un autre terminal**, exécutez :

```bash
python test/create_test_user.py
```

Un utilisateur temporaire sera créé :

```
Identifiant : test
Mot de passe : test
```

Connectez-vous avec ces identifiants, puis rendez-vous sur :

👉 [http://localhost:5001/auth/users/create](http://localhost:5001/auth/users/create)

Créez votre **propre utilisateur** avec un **rôle**.

---

### ❌ Supprimer l'utilisateur test

Une fois votre propre utilisateur créé, vous pouvez supprimer l'utilisateur `test` :

```bash
python test/delete_test_user.py
```

---

## 🛠️ Technologies

* Python / Flask
* SQLAlchemy
* MySQL / MariaDB

---

## 📂 Structure

```
gestion-fluides/
├── app/
├── test/
├── run.py
├── requirements.txt
└── README.md
```

---


