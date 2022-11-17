var context; // 객체 선언
var velocity; // 속도 (defult)
var angle; // 각도 (defult)
var ballVx; // 공의 가변 x값
var ballVy; // 공의 가변 y값
var ballX = 10; // 공의 x값 (defult)
var ballY = 250; // 공의 y값 (defult)
var ballRadius = 10; // 공의 반지름 (defult)
var score = 0; // 초기 점수 (defult)
var image = new Image(); // 이미지 생성 후 image 변수에 선언
image.src = "./imgs/lawn.png"; // image에 덮어씌울 이미지 경로 (바닥)
var backimage = new Image(); // 배경 이미지 생성 후 backimage 변수에 선언
backimage.src = "./imgs/net.png"; // image에 덮어씌울 이미지 경로 (바닥)
var timer; // 뱐수 선언 (이후에 새로고침 역할)

function drawBall() {
  // 공을 화면에 그림
  context.beginPath();
  context.arc(ballX, ballY, ballRadius, 0, 2.0 * Math.PI, true);
  // (ballX, ballY) 위치에, ballRadius 반지름의, 시작 각도 0, 360도로 원을 그림, 방식은 true
  context.fillStyle = "red"; // 원을 빨간색으로 채움 (원래는 텅빈 선으로 된 원임)
  context.fill(); // 색을 채우는 함수
}
function drawBackground() {
  // 배경을 화면에 그림
  context.drawImage(image, 0, 270); // (0, 270)에 image가 그려짐
  context.drawImage(backimage, 450, 60); // (450 ,60)에 image가 그려짐
}
function draw() {
  // 공, 배경을 처음처럼 그리는 함수
  context.clearRect(0, 0, 500, 300); // (0, 0)부터 가로:500 세로:300 만큼 화면을 지움
  drawBall(); // 공을 그림
  drawBackground(); // 배경을 그림
}
function init() {
  // 초기화하는 함수
  ballX = 10; // 공의 x값을 10으로 지정
  ballY = 250; // 공의 y값을 250으로 지정
  ballRadius = 10; // 공의 반지름을 10으로 지정
  context = document.getElementById("canvas").getContext("2d"); // canvas 요소에 2d속성과 함수를 부여
  draw(); // 싹다 삭제하고 공과 배경을 그림
}
function start() {
  // 모든걸 재시작하는 함수
  init(); // 화면 초기화
  velocity = Number(document.getElementById("velocity").value);
  // velocity 요소의 벨류 값을 가져옴 (이때 string으로 가져와서 Number함수 사용)
  angle = Number(document.getElementById("angle").value);
  // angle 요소의 벨류 값을 가져옴 (이때 string으로 가져와서 Number함수 사용)
  var angleR = (angle * Math.PI) / 100; // 계산 함수

  ballVx = velocity * Math.cos(angleR); // 계산 함수
  ballVy = -velocity * Math.sin(angleR); // 게산 함수

  draw(); // draw 함수 호출
  timer = setInterval(calculate, 100); // calculate 함수를 0.1초마다 반복
  return false; // false 리턴(?)
}
function calculate() {
  // 공의 현재 속도와 위치를 업데이트 함
  ballVy = ballVy + 1.98;
  ballX = ballX + ballVx; // ballX는 원래 x값에서, 변하는 x값을 더함
  ballY = ballY + ballVy; // ballY는 원래 y값에서, 변하는 y값을 더함

  if (ballX >= 450 && ballX <= 480 && ballY >= 60 && ballY <= 210) {
    // 만약 공의 x값이 450이상 480이하, y값이 60이상 210이하 라면
    score++; // 점수 +1
    document.getElementById("score").innerHTML = "점수: " + score;
    // score 요소의 값을 "점수: " + score로 바꿈
    clearInterval(timer); // 위에서 calculate 함수 반복하던걸 멈춤
  }
  if (ballY >= 300 || ballY < 0) {
    // 만약 공의 y값이 300 이상이거나, 0 미만이면
    clearInterval(timer); // 위에서 calculate 함수 반복하던걸 멈춤
  }
  draw(); // draw 함수 호출
}
