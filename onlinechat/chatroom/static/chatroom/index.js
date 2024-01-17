document.addEventListener("DOMContentLoaded", function () {
  document.getElementById("messageBar").style.display = "none";

  loadContacts();

  const inputMessage = document.getElementById("messageBar");
  inputMessage.addEventListener("keypress", function (event) {
    sendMessage(event, inputMessage);
  });
});

function loadContacts() {
  fetch("/contacts")
    .then((response) => response.json())
    .then((data) => {
      loadContacts2(data);
    });
}

function loadContacts2(data) {
  const currentUser = document.getElementById("current-user").innerHTML;
  data.forEach((element) => {
    const contact = document.createElement("div");
    contact.classList.add("contacts-item");
    if (element.user1 == currentUser) {
      contact.innerHTML = element.user2;
    } else {
      contact.innerHTML = element.user1;
    }
    contact.onclick = function () {
      buttonClick(contact);
    };
    document.querySelector(".contacts-list").appendChild(contact);
  });
}

function buttonClick(contact) {
  const chatUser = contact.innerHTML;
  document.getElementById("chatNav").innerHTML = chatUser;
  document.getElementById("messageBar").style.display = "block";
  document.getElementById("current-chat-username").innerHTML = chatUser;
  console.log(document.getElementById("current-chat-username").innerHTML);
  fetch("/chat/" + chatUser)
    .then((response) => response.json())
    .then((data) => {
      data.forEach((element) => {
        const chat = document.createElement("div");
        chat.innerHTML = element.message;
        if (element.sender == chatUser) {
          chat.classList.add("chat-item-left");
        } else {
          chat.classList.add("chat-item-right");
        }
        chat.classList.add("chat-item");
        document.querySelector(".chat-list").appendChild(chat);
      });
    });
  //load chat history and display it
}

function sendMessage(event, inputMessage) {
  const reciever = document.getElementById("chatNav").innerHTML;
  const message = inputMessage.value;
  if ((event.key === "Enter") & (message != "")) {
    fetch("/chat/" + reciever + "/", {
      method: "POST",
      body: JSON.stringify({
        message: message,
      }),
    });
    event.target.value = "";
  }
}
