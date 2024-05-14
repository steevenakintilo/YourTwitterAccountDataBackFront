import axios from "axios";
import React, { Component } from "react";
import "./styles.css"; // assuming your CSS file is named styles.css
import "./data.css"; // assuming your CSS file is named styles.css


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
        alert("Traitement de tes données patiente quelque minutes");
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
			<div className="backgroundcolour">
				{!this.state.TwitterData && (
          <div className="backgroundcolour">
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
        <div className="backgroundcolour">
          <div className="mainrectangle">
            <img src={this.state.TwitterData.jsonData.ProfilePicture} alt="Profile Picture" />
            <h4><span className="lightext">Ton username est </span> <span class="lightext2"> {this.state.TwitterData.jsonData.AccountUsername}</span></h4> 
            <h4><span className="lightext">L'ID de ton compte est </span> <span class="lightext2"> {this.state.TwitterData.jsonData.AccountId}</span></h4> 
            <h4><span className="lightext">Tu as crée ton compte le </span> <span class="lightext2"> {this.state.TwitterData.jsonData.AccountCreationDate}</span></h4> 
            <h4><span className="lightext">Ton compte a  </span> <span class="lightext2"> {this.state.TwitterData.jsonData.AccountAgeInDay}</span> jours <span className="lightext" jours></span></h4> 
          </div>
          <div className="container">
            <div className="rectangle">
              <h4><span className="lightext">Depuis la création de ton compte tu as fait au total: </span></h4> 
              <h4><span className="lightext2"> {this.state.TwitterData.jsonData.Nb_of_tweet_total} </span> <span class="lightext1"> tweets totaux "tweets,commentaires et rts compris"</span></h4> 
              <h4><span className="lightext2"> {this.state.TwitterData.jsonData.Nb_of_tweet} </span> <span class="lightext1"> tweets </span></h4> 
              <h4><span className="lightext2"> {this.state.TwitterData.jsonData.Nb_of_comment} </span> <span class="lightext1"> commentaires</span></h4> 
              <h4><span className="lightext2"> {this.state.TwitterData.jsonData.Nb_of_rt} </span> <span class="lightext1"> rts</span></h4> 
              
            </div>
            <div className="rectangle">
              <h4><span className="lightext">Ce qui donne une moyenne de: </span></h4> 
              <h4><span className="lightext2"> {this.state.TwitterData.jsonData.Nb_of_all_tweet_made_on_average} </span> <span class="lightext1"> tweets totaux "tweets,commentaires et rts compris" par </span> <span className="lightext2"> {this.state.TwitterData.jsonData.Nb_of_all_tweet_made_on_average_time} </span></h4> 
              <h4><span className="lightext2"> {this.state.TwitterData.jsonData.Nb_of_tweet_made_on_average} </span> <span class="lightext1"> tweets par</span> <span className="lightext2"> {this.state.TwitterData.jsonData.Nb_of_tweet_made_on_average_time} </span></h4> 
              <h4><span className="lightext2"> {this.state.TwitterData.jsonData.Nb_of_comment_made_on_average} </span> <span class="lightext1"> commentaires par</span> <span className="lightext2"> {this.state.TwitterData.jsonData.Nb_of_comment_made_on_average_time} </span></h4> 
              <h4><span className="lightext2"> {this.state.TwitterData.jsonData.Nb_of_rt_made_on_average} </span> <span class="lightext1"> rts par</span> <span className="lightext2"> {this.state.TwitterData.jsonData.Nb_of_rt_made_on_average_time} </span></h4> 
            </div>
  
          </div>

          <div className="longrectangle">
            <h4><span className="lightext">Niveau écriture voici le résultat: </span></h4> 
            <h4><span className="lightext2"> {this.state.TwitterData.jsonData.Nb_of_word} </span> <span class="lightext1"> mots</span></h4> 
            <h4><span className="lightext2"> {this.state.TwitterData.jsonData.Nb_of_unique_word} </span> <span class="lightext1"> mots différents </span></h4> 
            <h4><span className="lightext2"> {this.state.TwitterData.jsonData.Nb_of_word_on_average} </span> <span class="lightext1"> mots par tweets en moyenne</span></h4> 
            <h4><span className="lightext2"> {this.state.TwitterData.jsonData.Nb_of_char} </span> <span class="lightext1"> caractéres</span></h4> 
            <h4><span className="lightext2"> {this.state.TwitterData.jsonData.Nb_of_char_on_average} </span> <span class="lightext1"> caractéres en moyenne </span></h4> 
          </div>
          
          <div className="PetitPrincerectangle">
            <h4><span className="lightext">En comparaison avec le Petit Prince de Antoine de Saint-Exupéry: </span></h4> 
            <h4><span className="lightext1"> Le livre à </span> <span class="lightext2"> 14180 </span> <span class="lightext1"> mots et </span> <span class="lightext2"> 71595 </span> <span class="lightext1"> caractéres </span></h4> 
            {this.state.TwitterData.jsonData.Nb_of_time_you_wrote_le_petit_prince_by_char < 1 && (
              <h4><span className="lightext1"> Tu as donc écrit </span> <span class="lightext2"> {1 - this.state.TwitterData.jsonData.Nb_of_time_you_wrote_le_petit_prince_by_word} </span> <span class="lightext1"> fois moins de mots et </span> <span class="lightext2"> {1 - this.state.TwitterData.jsonData.Nb_of_time_you_wrote_le_petit_prince_by_char} </span> <span class="lightext1"> fois moins de caractéres que le livre</span></h4> 
            )}
            {this.state.TwitterData.jsonData.Nb_of_time_you_wrote_le_petit_prince_by_char >= 1 && (
              <h4><span className="lightext1"> Tu as donc écrit </span> <span class="lightext2"> {this.state.TwitterData.jsonData.Nb_of_time_you_wrote_le_petit_prince_by_word} </span> <span class="lightext1"> fois plus de mots et </span> <span class="lightext2"> {this.state.TwitterData.jsonData.Nb_of_time_you_wrote_le_petit_prince_by_char} </span> <span class="lightext1"> fois plus de caractéres que le livre</span></h4> 
            )}
            
          </div>
          
          <div className="tweetstatrectangle">
              <h4><span className="lightext">Depuis la création de ton compte tu as eu au total: </span></h4> 
              <h4><span className="lightext2"> {this.state.TwitterData.jsonData.Nb_of_like} </span> <span class="lightext1"> likes</span></h4> 
              <h4><span className="lightext2"> {this.state.TwitterData.jsonData.Nb_of_rts} </span> <span class="lightext1"> rts</span></h4> 
              <h4><span className="lightext">Ce qui fait une moyenne de: </span></h4> 
              <h4><span className="lightext2"> {this.state.TwitterData.jsonData.Nb_of_like_on_average} </span> <span class="lightext1"> likes par tweets</span></h4> 
              <h4><span className="lightext2"> {this.state.TwitterData.jsonData.Nb_of_rt_on_average} </span> <span class="lightext1"> rts par tweets</span></h4> 
          </div>
          <div className="lightext">Top 5 de tes tweets les plus liké</div>
          <ul>
            {this.state.TwitterData.jsonData.Top5MostLikedTweetUrl.slice(0, 5).map((tweetID, index) => (
                <li key={index}>
                  <a className="styles.body" href={tweetID} target="_blank"> Clique ici pour le voir </a>
                </li>
              ))}
            <br></br>
          </ul>
          <ul>
            <div className="textrectangle">
              <h4><span className="lightext">Depuis la création de ton compte tu as répondu à</span> <span className="lightext2"> {this.state.TwitterData.jsonData.UniqueRepliedUser} </span> personnes différentes</h4> 
              <h4 className="lightext">Voici le top 5 des personnes à qui tu as le plus répondu</h4>
              {this.state.TwitterData.jsonData.Top5RepliedUser.slice(0, 5).map((user, index) => (
                <li key={index}>
                  <h4><span className="lightext">Tu as répondu </span> <span className="lightext2"> {this.state.TwitterData.jsonData.Top5RepliedUserNb[index]} </span> <span className="lightext"> fois à </span> <span className="lightext2"> {this.state.TwitterData.jsonData.Top5RepliedUser[index]} </span> <span className="lightext"> ce qui fait </span> <span className="lightext2"> {this.state.TwitterData.jsonData.Top5RepliedUserPercent[index]} </span> <span className="lightext"> % de tes commentaires </span></h4>
                </li>
              ))}
            </div>
          </ul>
          <br></br>
          <ul>
            <div className="dmrectangle">
              <h4><span className="lightext">Tu as dm</span> <span className="lightext2"> {this.state.TwitterData.jsonData.UniqueDMedUser} </span> personnes différentes</h4> 
              <h4><span className="lightext">Tu as reçu</span> <span className="lightext2"> {this.state.TwitterData.jsonData.Nb_of_dm_received} </span> dm et tu en as envoyé <span className="lightext2"> {this.state.TwitterData.jsonData.Nb_of_dm_send} </span></h4> 
              <h4 className="lightext">Voici le top 5 des personnes à qui tu as le plus parlé en dm</h4>
              {this.state.TwitterData.jsonData.Top5RepliedUser.slice(0, 5).map((user, index) => (
                <li key={index}>
                  <h4><span className="lightext2"> {this.state.TwitterData.jsonData.Top5DMedUser[index]} </span> <span className="lightext"> : </span> <span className="lightext2"> {this.state.TwitterData.jsonData.Top5DMedUserNb[index]} </span> <span className="lightext"> ce qui représente </span> <span className="lightext2"> {this.state.TwitterData.jsonData.Top5DMedUserPercent[index]} </span> <span className="lightext"> % de tes dm </span></h4>
                </li>
              ))}
              <h4><span className="lightext">Tu as donc envoyé en moyenne </span> <span className="lightext2"> {this.state.TwitterData.jsonData.Nb_of_dm_send_on_average} </span> <span className="lightext"> dm par </span> <span className="lightext2"> {this.state.TwitterData.jsonData.Nb_of_dm_send_on_average_time} </span> et a reçu <span className="lightext2"> {this.state.TwitterData.jsonData.Nb_of_dm_received_on_average} </span> <span className="lightext"> dm par </span> <span className="lightext2"> {this.state.TwitterData.jsonData.Nb_of_dm_received_on_average_time} </span></h4>
            </div>
          </ul>
          <br></br>
          <div className="likerectangle">
            <h4><span className="lightext">Tu as liké </span> <span className="lightext2"> {this.state.TwitterData.jsonData.Nb_of_tweet_liked} </span> <span class="lightext1"> tweets ce qui fait une moyenne de </span> <span className="lightext2"> {this.state.TwitterData.jsonData.Nb_of_tweet_liked_on_average} </span> <span className="lightext"> likes par </span> <span className="lightext2"> {this.state.TwitterData.jsonData.Nb_of_tweet_liked_on_average_time} </span></h4> 
          </div>
          
          <ul>            
            {/* <img src={this.state.TwitterData.jsonData.ProfilePicture} alt="Profile Picture" />
             */}
            {/* {<img src={this.state.TwitterData.jsonData.ProfilePicture} alt="Profile Picture"/>} */}
            {/* {<img src="https://pbs.twimg.com/profile_images/1505596783686295554/N6F0fVEM.jpg" alt="Profile Picture" style={{ width: '50px', height: '50px' }} />} */}
            {/* <li>Property 1: {this.state.TwitterData.jsonData.AccountId}</li>
            <li>Property 2: {this.state.TwitterData.jsonData.AccountAgeInDay}</li> */}
            {/* Add more properties as needed */}
          </ul>
        </div>
      )}
			</div>
		);
	}
}

export default StartPage;
