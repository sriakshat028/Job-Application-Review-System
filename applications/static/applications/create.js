var countryStateInfo = {
    USA: {
      California: {
        "Los Angeles": ["90001", "90002", "90003", "90004"],
        "San Diego": ["92093", "92101"],
      },
      Texas: {
        Dallas: ["75201", "75202"],
        Austin: ["73301", "73344"],
      },
    },
    Germany: {
      Bavaria: {
        Munich: ["80331", "80333", "80335", "80336"],
        Nuremberg: ["90402", "90403", "90404", "90405"],
      },
      Hessen: {
        Frankfurt: ["60306", "60308", "60309", "60310"],
        Surat: ["55246", "55247", "55248", "55249"],
      },
    },
  };

window.onload = function () {
const countrySelection = document.querySelector("#Country"),
    stateSelection = document.querySelector("#State"),
    citySelection = document.querySelector("#City"),
    zipSelection = document.querySelector("#Zip");

    for (let country in countryStateInfo) {
      countrySelection.options[countrySelection.options.length] = new Option(
          country,
          country
        );
    }
      
      countrySelection.onchange = (e) => {
        stateSelection.disabled = false;
        stateSelection.length = 1;
        citySelection.length = 1;
        zipSelection.length = 1;
    
        
        for (let state in countryStateInfo[e.target.value]) {
          stateSelection.options[stateSelection.options.length] = new Option(
            state,
            state
          );
        }
      }

      stateSelection.onchange = (e) => {
        citySelection.disabled = false;

        citySelection.length = 1;
        zipSelection.length = 1; 
        for (let city in countryStateInfo[countrySelection.value][e.target.value]) {
          citySelection.options[citySelection.options.length] = new Option(
            city,
            city
          );
        }
      };

      citySelection.onchange = (e) => {
        zipSelection.disabled=false
        zipSelection.length = 1
        
        let zips = countryStateInfo[countrySelection.value][stateSelection.value][e.target.value];

        for(let i=0;i < zips.length;i++){
            zipSelection.options[zipSelection.options.length] = new Option(
                zips[i],
                zips[i]
            );
        }
      };
};

var edu_count=1;
function add_education(){
    edu_count+=1
    html='<label>Institute: </label>\
    <input type="text" name="institute'+edu_count+'">\
    <label>Degree: </label>\
    <select name="degree'+edu_count+'">\
       <option>-- Select Degree --</option>\
       <option>Associate Degree</option>\
       <option>Bachelor\'s Degree</option>\
       <option>Master\'s Degree</option>\
       <option>Doctoral Degree</option>\
    </select>\
    <label>Course: </label>\
    <input type="text" name="course'+edu_count+'">\
    <label >Start Date: </label>\
    <input type="date" name="start_date'+edu_count+'">\
    <label >End Date: </label>\
    <input type="date" name="end_date'+edu_count+'">\
    <br>'
     
    var edu=document.getElementById('education')
    edu.insertAdjacentHTML( 'beforeend', html)
}

var exp_count=1
function add_experience(){
  exp_count+=1
  html='<label>Company: </label>\
  <input type="text" name="company'+exp_count+'">\
  <label>Role: </label>\
  <input type="text" name="role'+exp_count+'">\
  <label >Start Date: </label>\
  <input type="date" name="start_date'+exp_count+'">\
  <label >End Date: </label>\
  <input type="date" name="end_date'+exp_count+'">\
  <label>Responsibilities: </label>\
  <textarea name="responsibilities'+exp_count+'"></textarea>\
  <br>'

  var exp=document.getElementById('experience')
  exp.insertAdjacentHTML( 'beforeend', html)
}

var skill_count=1
function add_skills(){
  skill_count+=1
  html='<input name="skill'+skill_count+'">\
  <br>'

  var skill=document.getElementById('skills')
  skill.insertAdjacentHTML( 'beforeend', html)
}
