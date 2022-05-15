import random
import json
import os


def backup_game(json_data):
    json_file = open("sauvegarde.json", "w")
    json.dump(json_data, json_file, indent=2)
    json_file.close()


def load_backup():
    json_file = open("sauvegarde.json", "r")
    json_data = json.load(json_file)
    json_file.close()
    json_data["labyrinth"][json_data["li"]][json_data["co"]]["content"] = "J"
    return json_data


def clear_backup():
    try:
        os.remove("sauvegarde.json")
    except FileNotFoundError:
        pass  # Pas d'erreur si le fichier n'existe pas puisqu'on voulait le supprimer
