# / var userAnswer = readlineSync.question(questionOne);
# // var readlineSync = require('readline-sync');
# // var userName = readlineSync.question('may I have your name? ')
# // console.log('userName'); //Ctrl + Cmd + /

# // var welcomeMessage = 'welcome'+ userName; //string concatination
# // console.log(welcomeMessaage
# // var readlineSync = require('readline-sync');

# // var score = 0;

# // var questionTwo = 'Am I from the city mirzapur ';
# // var answerTwo = 'no';
# //  var score = 0;
# // var questionOne = 'am I older than 25?';
# // var answerOne ='yes';
# // function play(question,answer) {

# // //input
# // console.log('you entered' + userAnswer);

# // //processing
# // if (userAnswer === answer) {
# //   // output
# //   console.log('you are right!');
# //   score = score + 1;
# //   console.log('score is:' + score)
# // } else {
# //   // output
# //   console.log('you are wrong!');
# //   score = score - 1;
# //   console.log('score is:'+ score)
# // }
# // } 

# //functions

# // function add(numberOne,numberTwo){
# //   console.log('numberOne;', numberOne,'numberTwo;',numberTwo)
# //   var sum = numberOne + numberTwo;
# //   return sum;
# // }

# // //use the function

# // var result = add(2,5);
# // console.log('the sum of 2 and 5 is' + result);
# // console.log(add(2,9));

# // var readlineSync = require('readline-sync');

# // var score = 0;

# // function play(question,answer){
# //   var userAnswer = readlineSync.question(question);

# //   if (userAnswer ===answer){
# //     console.log('you were right!');
# //     score = score + 1;
# //   } else{
# //     console.log('you were wrong!');
# //     score = score - 1;
#   // console.log('score is;'+ score)
# //   }
# // }
# // //calling the function

# // play('where do I work?','microsoft');

# // play('where do I live?','banglore')

# // console.log('your score is ',score)
# // play(questionOne,answerOne)

# // for (var i=0; i<5; i=i+1){
# //   console.log('shivani rathod')
# // }
# // 

# // function log(data){
# //   console.log(data)
# // }
# // var groceryList = ['milk','eggs','vadapav','samosa','flowers'];
# // for (var i=0; i< 5;i++) {
# //   console.log(groceryList[i]);
# // }

# // console.log(groceryList[0]);
# // console.log(groceryList[2]);
# // console.log(groceryList[4]);
# // //last item
# // var howLongIsThisArray = groceryList.length
# // console.log(howLongIsThisArray)
# // console.log(groceryList[groceryList.length-1])
# // 

# // var superman = {
# //   name: 'superman',
# //   power:'flight',
# //   costumeColor:'blue',
# //   strength:10000,
# //   stealth:0,
# //   intelligince:100,
# // }


# // var batman = {
# //   name:'batman',
# //   power:'martial arts',
# //   costumecolor:'black',
# //   strength:100,
# //   stealth:100,
# //   intelligence:1000,
# // }

# // console.log(superman.strength);

# // console.log(batman.strength);

# // console.log(superman.strength > batman.strength)


# // var superheroes = [superman,batman];

# // for (var i=0; i<superheroes.length; i++) {
# //   var currentHero = superheroes[i];
# //   console.log(currentHero.name);
# // }

# // const { question } = require('readline-sync');
# // var readlineSync = require('readline-sync');
# // var score = 0;
# // var userName = readlineSync.question('whats your name?');
# // console.log('welcome'+userName+'to do you know shivani')

# // //play function
# // function play(question,answer) {
# //   var userAnswer = readlineSync.question(question);
# //   if (userAnswer === answer){
# //     console.log('right!')
# //     score = score + 1;
# //     // console.log('current scores;',score);
# //     // console.log('---------')
# //   } else {
# //     console.log('wrong!');
# //   }
# //  console.log('current scores;',score);
# //   console.log('-------')
# // }
# // var question = [{
# //   question:'where do i live?',
# //   answer:'pune'
  
# // },
# // {
# //   question:'where do i studied?',
# //   answer:'software'
# // }];

# // //loop

# // for (var i=0; i<question.length;i++) {
# //   var currentQuestion = question[i];
# //   play(currentQuestion.question,currentQuestion.answer)
# // }
# // console.log('yay! you scored:',score)