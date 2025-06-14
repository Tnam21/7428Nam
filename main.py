<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <title>Makeup Game for Kids</title>
  <style>
    body {
      text-align: center;
      background-color: #fce4ec;
      font-family: 'Comic Sans MS', cursive;
    }
    h1 {
      color: #d81b60;
    }

    .face {
      margin: 20px auto;
      width: 200px;
      height: 250px;
      background-color: #ffe0b2;
      border-radius: 50% / 60%;
      position: relative;
    }

    .eye {
      width: 20px;
      height: 20px;
      background-color: #000;
      border-radius: 50%;
      position: absolute;
      top: 60px;
    }
    .eye.left {
      left: 50px;
    }
    .eye.right {
      right: 50px;
    }

    .lip {
      width: 60px;
      height: 20px;
      background-color: #e91e63;
      border-radius: 0 0 50px 50px;
      position: absolute;
      bottom: 40px;
      left: 70px;
    }

    .blush {
      width: 30px;
      height: 15px;
      background-color: #f48fb1;
      border-radius: 50%;
      position: absolute;
      top: 130px;
    }
    .blush.left {
      left: 20px;
    }
    .blush.right {
      right: 20px;
    }

    .controls {
      margin-top: 30px;
    }

    label {
      margin-right: 10px;
    }

    select {
      padding: 5px;
      margin: 10px;
    }
  </style>
</head>
<body>
  <h1>🎨 Game Makeup Dễ Thương 🎀</h1>
  <div class="face">
    <div class="eye left"></div>
    <div class="eye right"></div>
    <div class="lip" id="lip"></div>
    <div class="blush left" id="blush-left"></div>
    <div class="blush right" id="blush-right"></div>
  </div>

  <div class="controls">
    <div>
      <label for="lip-color">Màu Son:</label>
      <select id="lip-color">
        <option value="#e91e63">Hồng</option>
        <option value="#f44336">Đỏ</option>
        <option value="#9c27b0">Tím</option>
        <option value="#ff9800">Cam</option>
      </select>
    </div>

    <div>
      <label for="blush-color">Má Hồng:</label>
      <select id="blush-color">
        <option value="#f48fb1">Hồng Nhạt</option>
        <option value="#ec407a">Hồng Đậm</option>
        <option value="#f06292">Hồng Đào</option>
      </select>
    </div>

    <div>
      <label for="eye-color">Màu Mắt:</label>
      <select id="eye-color">
        <option value="#000000">Đen</option>
        <option value="#3f51b5">Xanh</option>
        <option value="#795548">Nâu</option>
        <option value="#607d8b">Xám</option>
      </select>
    </div>
  </div>

  <script>
    const lip = document.getElementById("lip");
    const blushLeft = document.getElementById("blush-left");
    const blushRight = document.getElementById("blush-right");
    const eyes = document.querySelectorAll(".eye");

    document.getElementById("lip-color").addEventListener("change", function () {
      lip.style.backgroundColor = this.value;
    });

    document.getElementById("blush-color").addEventListener("change", function () {
      blushLeft.style.backgroundColor = this.value;
      blushRight.style.backgroundColor = this.value;
    });

    document.getElementById("eye-color").addEventListener("change", function () {
      eyes.forEach(eye => {
        eye.style.backgroundColor = this.value;
      });
    });
  </script>
</body>
</html>
