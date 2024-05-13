import axios from "axios";
import React, { Component } from "react";
import "./styles.css"; // assuming your CSS file is named styles.css


class StartPage extends Component {
	state = {
		selectedFile: null,
	};
  
	onFileChange = (event) => {
    const file = event.target.files[0];
    //console.log("fff " , file ,  "    ", file.name.includes(".zip"));
		if (file && file.name.includes(".zip") === true) {
			this.setState({
				selectedFile: file,
			});
		} else {
			alert("Please select a ZIP file.");
    }
	};

	onFileUpload = () => {
    if (this.state.selectedFile) {
        const formData = new FormData();
        formData.append(
            "myFile",
            this.state.selectedFile,
            this.state.selectedFile.name
        );
        console.log("Doing");
        //console.log(this.state.selectedFile);

        fetch("http://127.0.0.1:8000/DownloadAndGenerateData", {
            method: 'POST',
            body: formData,
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            //Handle successful response
            console.log('File uploaded successfully.');
            //const TwitterData = response.json();
            //console.log("Whole response " , TwitterData);
            return response.json();
            
        })

        .then(TwitterData => {
          // Update state with fetched Twitter data
          this.setState({ TwitterData });
          //dataToDisplay = TwitterData.jsonData;
          console.log("CACA response ", TwitterData.jsonData);
          //history.push(`/DisplayData/${TwitterData.jsonData}`);
        })

        .catch(error => {
            // Handle error
            console.error('There was a problem with the fetch operation:', error);
        });
    } else {
        alert("Please select a file before uploading.");
              
    }
};
  
	fileData = () => {
		if (this.state.selectedFile) {
			return (
				<div>
				</div>
			);
		} else {
			return (
				<div>
					<br />
				</div>
			);
		}
	};
  
	render() {
		return (
			<div>
				{!this.state.TwitterData && (
          <div>
            <h1 className="styles.body">Upload ton archive twitter puis clique sur envoyer</h1>
            <br></br>
            <a className="styles.body" href="https://help.twitter.com/fr/managing-your-account/how-to-download-your-x-archive" target="_blank"> Clique ici pour télécharger ton archive </a>
            <br></br>
            <br></br>
            <br></br>
            <h2>L'archive vous seras envoyé par mail dans 1J puis vous n'aurez plus qu'a la télécharger et l'upload sur le site</h2>
            <br></br>
            <br></br>
            <br></br>
            <input
              type="file"
              onChange={this.onFileChange}
              accept=".zip"
            />
            <button onClick={this.onFileUpload}>
              Envoyer! 
            </button>
            <br></br>
            <br></br>
            <br></br>
            <h2>Toutes vos data sont supprimées après l'affichage de vos données</h2>

          </div>
        )}
				{this.fileData()}
        {this.state.TwitterData && (
        <div>
          <h2>Twitter Data</h2>
          <ul>
            <li>Property 1: {this.state.TwitterData.jsonData.AccountId}</li>
            <li>Property 2: {this.state.TwitterData.jsonData.AccountAgeInDay}</li>
            {/* Add more properties as needed */}
          </ul>
        </div>
      )}
			</div>
		);
	}
}

export default StartPage;
