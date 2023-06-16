<h1>This is the repository belong to Machine Learning Path</h1>

<h2>This is our current progress</h2>
<p>
  <ol>
    <li>
      <strong> Datasets (100%) </strong>
      <p> Our datasets consists 10 class of ingredients, such as chicken, red onion, garlic, 
        goat meat, catfish, tofu, tempe, egg, and shrimp with 240 training and 60 testing 
        data for each class
    </p>
    </li>
    <li> 
      <strong> Model(100%)  </strong>
      <p> we've been made our main model, that could classify an ingredient for cooking by taking the image of the ingredient. our model is made by transfer 
        learning using the MobileNetV2 architecture </p>
    </li>
    <li> 
      <strong> Accuracy  </strong>
      <p> Our train accuracy has reach 92% and 80% on test subject. at this point, it can be conclude 
        that out model is working properly to classify the image of the food ingredient  </p>
    </li>
    <li> 
      <strong> Conversion </strong>
      <p> to deploy the model, we convert our model type to .h5  </p>
    </li>
    <li> 
      <strong> Deploy (90%) </strong>
      <p> We use Flask API and Docker Container for deploying to POSTMAN </p>  
    </li>
    <li>
        <strong>Future plant</strong>
        <ul>
            <li>
                make our model accuracy more higher to at least around 90 %  
            </li>
            <li>
                make the recommendation to recommend the user about the recipe of food that they  want to cook 
            </li>
            <li>
                make the Object detection to classify the image of ingredient that have
                specific shape such as ginger,coriander, etc that could help user to know what kind 
                of ingredient it is 
            </li>
            <li>
                make summary system that can make a summary base on article about food
            </li>
        </ul>
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
