const options = document.querySelectorAll(".options");
//Set player and computer score at 0
let playerScore = 0;
let computerScore = 0;

options.forEach((option) => {
  option.addEventListener("click", function () {

    const playerInput = this.textContent;

    //Define the computers options and pick one at random
    const computerOptions = ["Rock", "Paper", "Lightsaber"];
    const computerInput = computerOptions[Math.floor(Math.random() * 3)];

    //Compare inputs between player and computer
    compareInputs(playerInput, computerInput);
    updateScore();
    if (checkWinner()) {
      playerScore = computerScore = 0;
      updateScore();
    }
  });
});

//If player and computer choose the same, don't increase either score
function compareInputs(playerInput, computerInput) {
  const result = document.querySelector('.result')
  const currentMatch = `${playerInput} vs ${computerInput}`;
  if (playerInput === computerInput) {
    return;
  }

  //Check winner based on choice
  if (playerInput === "Rock") {
    if (computerInput === "Lightsaber") {
      playerScore++;
      result.setContent = 'You won that round!';
      res
    } else {
      computerScore++;
      result.setContent = 'Computer won that round!';
    }
  }
  //Check winner based on choice
  else if (playerInput === "Paper") {
    if (computerInput === "Rock") {
      playerScore++;
      result.setContent = 'You won that round!';
    } else {
      computerScore++;
      result.setContent = 'Computer won that round!';
    }
  }
  //Check winner based on choice
  else {
    if (computerInput === "Paper") {
      playerScore++;
      result.setContent = 'You won that round!';
    } else {
      computerScore++;
      result.setContent = 'Computer won that round!';
    }
  }
}

//Update the score on the webpage
function updateScore() {
  document.getElementById("player_score").textContent = playerScore;
  document.getElementById("computer_score").textContent = computerScore;
}

//Check the winner and display popup with winner
function checkWinner() {
  if (playerScore === 5 || computerScore === 5) {
    const winner =
      playerScore === 5
        ? "You win the game! Congratulations!"
        : "Computer wins the game! Try again next time!";
    alert(winner);
    return true;
  }
  return false;
}
