const months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
 ];
  const weekdays = [
    "Sun",
    "Mon",
    "Tue",
    "Wed",
    "Thu",
    "Fri",
    "Sat"  
 ];
  
  const main = document.getElementById("main");
  
  // Mood Selector
  const moodSelector = document.querySelectorAll("#mood");
  moodSelector.forEach(mood => { mood.addEventListener("click", handleMoodClick)});
  
  
  function handleMoodClick() {  
    moodSelector.forEach(node => {
      node.classList.remove("fas")
      node.classList.add("far")
    })
      // Modify the mood color Variable
      // Get clicked mood color
      let color = getComputedStyle(this);
      console.log(color.color) // rgb(0,128,0)
      document.documentElement.style.setProperty('--moodColor',color.color)
      // remove class far 
      this.classList.remove("far")
      this.classList.add("fas")
     // <i class="fas fa-laugh"></i>
      
    
  }
  
  //Change of Color Handler
  function handleClickOnDay(event) {
    let color = getComputedStyle(document.documentElement).getPropertyValue('--moodColor');
  
    if (color == " #bbb") {
      console.log("igual")
    } else {
      event.target.setAttribute('style', `background-color: ${color}`)
      //event.target.classList.toggle("selected")
    }
  
  
  
  }
  
  
  months.forEach(month => {
    createMonthElement(month);
  });
  
  function createMonthElement(month) {
    let newDiv = document.createElement("div");
    newDiv.classList.add("one-third");
    newDiv.classList.add("column");
    let newSpan = document.createElement("span")
    newSpan.innerHTML = month;
    newSpan.setAttribute("id", "month");
    newDiv.appendChild(newSpan)
    main.appendChild(newDiv)
  
    createWeekHeader(newDiv);
    createDays(newDiv, month)
  };
  
  function createWeekHeader(div) {
    let newList = document.createElement("ul")
    newList.classList.add("weekdays")
  
    weekdays.forEach(day => {
      let newLi = document.createElement("li")
      newLi.innerText = day
      newList.appendChild(newLi)
    })
  
    div.appendChild(newList)
  };
  
  function getStartPosition(month) {
    return new Date(`${month} 1, 2020`).getDay();
  }
  
  function createDays(div, month) {
    let days = 31;
  
    let startingPos = getStartPosition(month) + 1;
  
    switch (month){
      case "April":
      case "June":
      case "September":
      case "November":
        days = 30;
        break;
      case "February":
        days = 29;
        break;
    };
  
    let newList = document.createElement("ul")
    newList.classList.add("days")
  
    startMonthAt(startingPos, newList);
  
    for( let i = 1; i <= days; i++){
      let newDay = document.createElement("li")
      newDay.innerText = i
      newDay.classList.add("dot")
      newDay.addEventListener("click", handleClickOnDay)
      newList.appendChild(newDay)    
    }
    
    div.appendChild(newList)  
  };
  function startMonthAt(emptyDays, list) {
    for( let i = 1; i < emptyDays; i++){
      let newDay = document.createElement("li") 
      newDay.innerText = " "
      list.appendChild(newDay)
      
    }
  }
  

let moodForm = document.querySelector('#mood_tracker')  
console.log(moodForm)

