package application;
	

import javafx.event.ActionEvent;
import java.io.File;
import javafx.application.Application;
import javafx.event.EventHandler;
import javafx.stage.Stage;
import javafx.scene.Scene;
import javafx.scene.layout.BorderPane;
import javafx.scene.layout.GridPane;
import javafx.geometry.Insets;
import javafx.geometry.Pos;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.TextArea;
import javafx.scene.layout.HBox;
import javafx.scene.layout.VBox;
import javafx.scene.paint.Color;
import javafx.scene.text.Font;
import javafx.stage.Stage;


public class CovidContact extends Application {
	
	private static Stage 		window;
	private static Label 		title, fNameLabel, lNameLabel, uniqueIDLabel, phoneNumberLabel, positivity;
	private static Button		addButton, removeButton, listButton, loadButton, saveButton, exitButton;
	private static TextArea		fNameTextArea, lNameTextArea, uniqueIDTextArea, phoneNumberTextArea, closeContactsTextArea;
	private static Controller 	control;
	
	@SuppressWarnings("unused")
	private static File file = new File("Contacts");
	
	public static void main(String[] args) {
		launch(args);
	}
	
	@Override
	public void start(Stage primaryStage) throws Exception {
		window = primaryStage;
		control = new Controller();
		window.setTitle("Covid Close Contacts");
		
		//Text Labels
		title = new Label("							-------------------------------- COVID CLOSE CONTACTS -------------------------------------");
		fNameLabel = new Label("Enter First Name:");
		lNameLabel = new Label("Enter Last Name:");
		uniqueIDLabel = new Label("Enter Unique ID:");
		phoneNumberLabel = new Label("Enter Phone No.:");
		positivity = new Label("Where we can no longer reach out with our hands, we must reach out with our hearts. Stay safe.");
		
		//Text Areas
		fNameTextArea = new TextArea();
		lNameTextArea = new TextArea();
		uniqueIDTextArea = new TextArea();
		phoneNumberTextArea = new TextArea();
		
		//First row of buttons
		addButton = new Button("ADD");
		removeButton = new Button("REMOVE");
		listButton = new Button("LIST");
		
		//Contacts text area
		closeContactsTextArea = new TextArea("Close contacts displayed here...");
		closeContactsTextArea.setPrefWidth(400);
		closeContactsTextArea.setPrefHeight(1000);
		
		//Second row of buttons
		loadButton = new Button("Load");
		saveButton = new Button("Save");
		exitButton = new Button("Exit");
		
		//First row of buttons functionality
		addButton.setOnAction(e-> control.addContactToList(fNameTextArea.getText(), lNameTextArea.getText(), uniqueIDTextArea.getText(), phoneNumberTextArea.getText()));
		removeButton.setOnAction(e-> control.removeContactFromList());
		listButton.setOnAction(new EventHandler<ActionEvent>() {
		@Override
		public void handle(ActionEvent event) {
			String allContacts = control.getContactList();
				closeContactsTextArea.setText(allContacts);
				}});
		
		//Second row of buttons functionality
		loadButton.setOnAction(e-> control.loadFile(closeContactsTextArea));
		saveButton.setOnAction(e-> control.saveFile("covidContacts.txt", closeContactsTextArea.getText()));
		exitButton.setOnAction(e-> control.exitApplication());
		
		//Create HBox's
		HBox r1 = new HBox(10);
		r1.getChildren().addAll(title);
		
		HBox message = new HBox(50);
		message.getChildren().addAll(positivity);
		message.setAlignment(Pos.CENTER);
		
		
		HBox r2 = new HBox(10);
		r2.getChildren().addAll(fNameLabel);
		r2.getChildren().addAll(fNameTextArea);
		r2.setAlignment(Pos.CENTER);
		
		HBox r3 = new HBox(10);
		r3.getChildren().addAll(lNameLabel);
		r3.getChildren().addAll(lNameTextArea);
		r3.setAlignment(Pos.CENTER);
		
		HBox r4 = new HBox(10);
		r4.getChildren().addAll(uniqueIDLabel);
		r4.getChildren().addAll(uniqueIDTextArea);
		r4.setAlignment(Pos.CENTER);
		
		HBox r5 = new HBox(10);
		r5.getChildren().addAll(phoneNumberLabel);
		r5.getChildren().addAll(phoneNumberTextArea);
		r5.setAlignment(Pos.CENTER);
		
		HBox r6 = new HBox(10);
		r6.getChildren().addAll(addButton, removeButton, listButton);
		r6.setAlignment(Pos.CENTER);
		
		HBox r7 = new HBox(10);
		r7.getChildren().addAll(closeContactsTextArea);
		r7.setAlignment(Pos.CENTER);
		
		HBox r8 = new HBox(10);
		r8.getChildren().addAll(loadButton, saveButton);
		r8.setAlignment(Pos.BOTTOM_LEFT);
		
		HBox r9 = new HBox(10);
		r9.getChildren().addAll(exitButton);
		r9.setAlignment(Pos.BOTTOM_RIGHT);
		
		//Define HBox layout
		VBox layout = new VBox(10);
		layout.setPadding(new Insets(20, 20, 20, 20));
		layout.getChildren().addAll(r1, message, r2, r3, r4, r5, r6, r7, r8 ,r9);
		
		//Create scene
		Scene scene = new Scene(layout, 800, 700, Color.BEIGE);
		window.setScene(scene);
		window.show();
		
		//Styling labels
		fNameLabel.setFont(Font.font(java.awt.Font.SERIF, 15));
		lNameLabel.setFont(Font.font(java.awt.Font.SERIF, 15));
		uniqueIDLabel.setFont(Font.font(java.awt.Font.SERIF, 15));
		phoneNumberLabel.setFont(Font.font(java.awt.Font.SERIF, 15));
		
		//Styling Buttons
		addButton.setFont(Font.font(java.awt.Font.SERIF, 15));
		removeButton.setFont(Font.font(java.awt.Font.SERIF, 15));
		listButton.setFont(Font.font(java.awt.Font.SERIF, 15));
		
		loadButton.setFont(Font.font(java.awt.Font.SERIF, 18));
		saveButton.setFont(Font.font(java.awt.Font.SERIF, 18));
		exitButton.setFont(Font.font(java.awt.Font.SERIF, 18));
		
	}
}
