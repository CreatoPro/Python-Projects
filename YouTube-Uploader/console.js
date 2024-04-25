const pause = async (milliseconds) =>
  new Promise((resolve) => setTimeout(resolve, milliseconds));

var buttons = document.querySelectorAll("#video-title");

const numberOfButtonsToClick = 2;
buttons.forEach((button, index) => {
  if (index < numberOfButtonsToClick) {
    button.click();
    console.log("Line 1");
    setTimeout(function () {
      document.querySelector("#step-badge-3").click();
      console.log("Line 2");
      setTimeout(function () {
        document.querySelector("#second-container-expand-button").click();
        console.log("Line 3");
        setTimeout(function () {
          document.querySelector("#done-button").click();
          console.log("Line 4");
          // Add more lines as needed
          setTimeout(function () {
            const close = document.querySelectorAll("div");

            close.forEach((div) => {
              if (div.textContent.trim() === "Close") {
                div.click();
              }
              console.log("Line 5");
              setTimeout(function () {
                console.log("Line 6");
              }, 10000);
            });
          }, 10000);
        }, 10000);
      }, 10000);
    }, 10000);
  }
});

var close = document.querySelectorAll("div");

close.forEach((div) => {
  if (div.textContent.trim() === "Close") {
    div.click();
  }
});
document.querySelector("#step-badge-3").click();
document.querySelector("#second-container-expand-button").click();
document.querySelector("#done-button").click();

const close = document.querySelectorAll("div");

close.forEach((div) => {
  if (div.textContent.trim() === "Close") {
    div.click();
  }
});
