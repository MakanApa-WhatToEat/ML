<h1>This is the repository belong to Machine Learning Path</h1>

<h2>This is our current progress</h2>
<p>
  <ol>
    <li>
      <strong> Datasets (100%) </strong>
      <p> Our datasets consists 10 class of ingredients, such as chicken, red onion, garlic, goat meat, catfish, tofu, tempe, egg, and shrimp </p>
    </li>
    <li> 
      <strong> Model(80%)  </strong>
      <p> Our model use transfer learning with MobileNetV2 architecture. In the future, we will create a CNN architecture</p>
    </li>
    <li> 
      <strong> Accuracy  </strong>
      <p> Our train accuracy has reach 92% and 80% on test subject </p>
    </li>
    <li> 
      <strong> Convertion </strong>
      <p> Our model has been converted to h5 type of model </p>
    </li>
    <li> 
      <strong> Deploy (20%) </strong>
      <p> We use Flask API and Docker Container for deploying to POSTMAN </p>  
    </li>
  </ol>
</p>

<hr>

<h2><b> How To Run The File </b></h2>
<p>
  <Strong> Using Docker </strong>
  <ol>
    <li> Clone the repository</li>
    <li> Run the Docker File in the API Folder</li>
  </ol>  
</p>
<p>
  <Strong> Using Environment in Visual Studio Code</strong>
  <ol>
    <li> Clone the repository</li>
    <li> Create Environment <b>(View -> Command Pallete -> Python:Create Environment)</b></li>
    <li> Run <b>.venv -> Scripts -> Activate.ps1 </b>(Make sure you have Powershell extension)</li>
    <li> Run <b>Terminal -> New Terminal </b></li>
    <li> Run <b>python install -r requirements.txt </b>(Skip this if the required library has been installed in your environment(.venv -> Library))
    <li> Run <b> python -m app.py </b> or <b> python -m flask run </b> </li>
  </ol>  
</p>
