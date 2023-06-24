function vacation(peopleCount, typeOfGroup, dayOfWeek) {
  let totalPrice;

  switch (typeOfGroup) {
    case "Students":
      if (dayOfWeek === "Friday") {
        totalPrice = peopleCount * 8.45;
      } else if (dayOfWeek === "Saturday") {
        totalPrice = peopleCount * 9.80;
      } else {
        totalPrice = peopleCount * 10.46;
      }

      if (peopleCount >= 30) {
        totalPrice -= totalPrice * 0.15;
      }
      break;

    case "Business":
      if (peopleCount >= 100) {
        peopleCount -= 10;
      }
      if (dayOfWeek === "Friday") {
        totalPrice = peopleCount * 10.9;
      } else if (dayOfWeek === "Saturday") {
        totalPrice = peopleCount * 15.6;
      } else {
        totalPrice = peopleCount * 16;
      }
      break;

    case "Regular":
      if (dayOfWeek === "Friday") {
        totalPrice = peopleCount * 15;
      } else if (dayOfWeek === "Saturday") {
        totalPrice = peopleCount * 20;
      } else {
        totalPrice = peopleCount * 22.5;
      }
      if (peopleCount >= 10 && peopleCount <= 20) {
        totalPrice -= totalPrice * 0.05;
      }
      break;
  }

  console.log(`Total price: ${totalPrice.toFixed(2)}`);
}

vacation(30, "Students", "Sunday");
