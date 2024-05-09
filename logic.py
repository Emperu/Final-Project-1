from PyQt5.QtWidgets import QMessageBox

john_votes = 0
jane_votes = 0
total_votes = 0
voter_ids = {}


def vote(candidate, id_code, window):
    global john_votes, jane_votes, total_votes, voter_ids

    if id_code in voter_ids:
        error_dialog = QMessageBox(window)
        error_dialog.setWindowTitle('Error')
        error_dialog.setText('<p style="color:red;">Error: This ID already voted.</p>')
        error_dialog.exec()
        return

    if candidate == 1:
        john_votes += 1
    elif candidate == 2:
        jane_votes += 1

    total_votes += 1
    voter_ids[id_code] = candidate
    print(f'John-{john_votes}, Jane-{jane_votes}, Total-{total_votes}')

# logic.py
def process_vote(id_code, candidate, window, labels):
    if id_code == "":
        return "Please enter an ID."

    if candidate == 0:
        return "Please select a candidate."

    vote(candidate, id_code, window)

    from logic import john_votes, jane_votes, total_votes
    labels[0].setText(f"John Votes: {john_votes}")
    labels[1].setText(f"Jane Votes: {jane_votes}")
    labels[2].setText(f"Total Votes: {total_votes}")

    return ""

