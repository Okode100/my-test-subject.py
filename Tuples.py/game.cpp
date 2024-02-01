#include <iostream>

int main() {
  // Initialize game state
  int player_health = 100;
  int enemy_health = 50;

  while (true) {
    // Update game state
    std::cout << "Player health: " << player_health << std::endl;
    std::cout << "Enemy health: " << enemy_health << std::endl;

    // Render game
    // (In this simple example, rendering is just printing to the console)

    // Check for user input
    std::cout << "Press 'a' to attack, 'q' to quit: ";
    char input;
    std::cin >> input;
    if (input == 'a') {
      // Attack logic goes here
      enemy_health -= 10;
      if (enemy_health <= 0) {
        std::cout << "You win!" << std::endl;
        break;
      }
    } else if (input == 'q') {
      // Quit logic goes here
      std::cout << "Thanks for playing!" << std::endl;
      break;
    }
  }

  return 0;
}