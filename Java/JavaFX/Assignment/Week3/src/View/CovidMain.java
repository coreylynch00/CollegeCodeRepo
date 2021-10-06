package View;
	
import java.util.ArrayList;

import Controller.Controller;
import javafx.application.Application;
import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.event.ActionEvent;
import javafx.event.EventHandler;
import javafx.geometry.Insets;
import javafx.geometry.Pos;
import javafx.scene.Group;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.ComboBox;
import javafx.scene.control.Label;
import javafx.scene.control.Tab;
import javafx.scene.control.TabPane;
import javafx.scene.control.TextArea;
import javafx.scene.layout.BorderPane;
import javafx.scene.layout.HBox;
import javafx.scene.layout.StackPane;
import javafx.scene.layout.VBox;
import javafx.scene.paint.Color;
import javafx.scene.text.Font;
import javafx.stage.Stage;


public class CovidMain extends Application {
	
	private static Label 		title, fNameLabel, lNameLabel, uniqueIDLabel, phoneNumberLabel, contact1Label, contact2Label, dateLabel, timeLabel, title2, title3;
	private static Button		addButton, removeButton, listButton, loadButton, saveButton, exitButton, reportButton, t2exitButton, listPositiveButton, savePositiveButton, loadPositiveButton, t3exitButton;
	private static TextArea		fNameTextArea, lNameTextArea, uniqueIDTextArea, phoneNumberTextArea, closeContactsTextArea, dateTextArea, timeTextArea, positiveContactsTextArea;
	private static ComboBox		contact1ComboBox, contact2ComboBox;
	private static Controller 	control;
	
	public static void main(String[] args) {
		launch(args);
	}
	
	
	@SuppressWarnings("unchecked")
	@Override
	public void start(Stage primaryStage) {
		primaryStage.setTitle("Covid Close Contacts");
		Group root = new Group();
		Scene scene = new Scene(root, 1000, 900, Color.WHITE);
		
		//Controller for event handler
		control = new Controller();
		
		//Panes
		TabPane tabPane = new TabPane();
		BorderPane mainPane = new BorderPane();	
		
		//Tab 1 Text Labels
		title = new Label("	------------------------------ COVID CLOSE CONTACTS ---------------------------------");
		fNameLabel = new Label("Enter First Name:");
		lNameLabel = new Label("Enter Last Name:");
		uniqueIDLabel = new Label("Enter Unique ID:");
		phoneNumberLabel = new Label("Enter Phone No:");
		
		//Tab 1 Text Areas
		fNameTextArea = new TextArea();
		lNameTextArea = new TextArea();
		uniqueIDTextArea = new TextArea();
		phoneNumberTextArea = new TextArea();
		
		//Tab 1 First row of buttons
		addButton = new Button("ADD");
		removeButton = new Button("REMOVE");
		listButton = new Button("LIST");
		
		//Tab 1 Contacts text area
		closeContactsTextArea = new TextArea("Contacts displayed here...");
		closeContactsTextArea.setPrefWidth(600);
		closeContactsTextArea.setPrefHeight(400);
		
		//Tab 1 Second row of buttons
		loadButton = new Button("Load");
		saveButton = new Button("Save");
		exitButton = new Button("Exit");
		
		
		//Tab 2 Labels
		contact1Label = new Label("Close Contact 1:");
		contact2Label = new Label("Close Contact 2:");
		dateLabel = new Label("Date of Contact (dd/mm/yy):");
		timeLabel = new Label("Time of Contact (00:00):");
		
		//Tab 2 Text Areas
		dateTextArea = new TextArea();
		dateTextArea.setPrefWidth(400);
		dateTextArea.setPrefHeight(30);
		timeTextArea = new TextArea();
		timeTextArea.setPrefWidth(400);
		timeTextArea.setPrefHeight(30);
		
		//Tab 2 Button
		reportButton = new Button("Report");
		t2exitButton = new Button("Exit");
		
		//Tab 2 Combo Box
		contact1ComboBox = new ComboBox<String>();
		contact1ComboBox.setPrefWidth(300);
		contact1ComboBox.setPrefHeight(20);
		contact2ComboBox = new ComboBox<String>();
		contact2ComboBox.setPrefWidth(300);
		contact2ComboBox.setPrefHeight(20);
		
		//contact1ComboBox.setItems((ObservableList)control.comboBoxArray());
		//contact2ComboBox.setItems((ObservableList)control.comboBoxArray());
		//contact1ComboBox.getItems().addAll(control.comboBoxArray());
		//contact2ComboBox.getItems().addAll(control.comboBoxArray());
		
		//Hard coded names in comboBox
		contact1ComboBox.setItems(FXCollections.observableArrayList(new String("Ber Lynch"), new String ("Corey Lynch"), new String ("Jake Lynch"), new String ("Mollie O Mahony"), new String ("Marie Sexton"), new String ("Paul Murphy"), new String ("David Ahern")));
		contact2ComboBox.setItems(FXCollections.observableArrayList(new String("Ber Lynch"), new String ("Corey Lynch"), new String ("Jake Lynch"), new String ("Mollie O Mahony"), new String ("Marie Sexton"), new String ("Paul Murphy"), new String ("David Ahern")));
		
		//Tab 2 Title
		title2 = new Label("-----Specify 2 Persons Who Engaged In a Close Contact Occurance Here:-----");
		
		
		//Tab 3 Title
		title3 = new Label("-----*REPORTED* Covid-19 Positive Contacts, Whom Were In Close Contact-----");
		
		//Tab 3 Text Area
		positiveContactsTextArea = new TextArea("Positive contacts displayed here...");
		positiveContactsTextArea.setPrefWidth(600);
		positiveContactsTextArea.setPrefHeight(400);
		
		//Tab 3 Buttons
		listPositiveButton = new Button("List");
		savePositiveButton = new Button("Save");
		loadPositiveButton = new Button("Load");
		t3exitButton = new Button("Exit");
		
		//Button Functionality
		//TAB 1 FIRST ROW
		addButton.setOnAction(e-> control.addContactToList(fNameTextArea.getText(), lNameTextArea.getText(), uniqueIDTextArea.getText(), phoneNumberTextArea.getText()));
		removeButton.setOnAction(e-> control.removeContactFromList());
		listButton.setOnAction(new EventHandler<ActionEvent>() {
		@Override
		public void handle(ActionEvent event) {
			String allContacts = control.getContactList();
				closeContactsTextArea.setText(allContacts);
				}});
		
		//TAB 1 SECOND ROW
		loadButton.setOnAction(e-> control.loadFile(closeContactsTextArea));
		saveButton.setOnAction(e-> control.saveFile("covidContacts.txt", closeContactsTextArea.getText()));
		exitButton.setOnAction(e-> control.exitApplication());
		
		//TAB 2
		System.out.println(contact1ComboBox);
		reportButton.setOnAction(e -> control.addPositiveToList(contact1ComboBox.getPromptText(), contact2ComboBox.getPromptText(), dateTextArea.getText(), timeTextArea.getText()));
		t2exitButton.setOnAction(e-> control.exitApplication());
		
		//TAB 3
		listPositiveButton.setOnAction(new EventHandler<ActionEvent>() {
			@Override
			public void handle(ActionEvent event) {
				String allPositiveContacts = control.getPositiveContactList();
				positiveContactsTextArea.setText(allPositiveContacts);
					}});;

		savePositiveButton.setOnAction(e-> control.savePositiveContacts("covidPositiveContacts.txt", positiveContactsTextArea.getText()));
		loadPositiveButton.setOnAction(e -> control.loadPositiveFile(positiveContactsTextArea));
		t3exitButton.setOnAction(e-> control.exitApplication());
		
		
		//CREATE TABS
//#############################################################################################################################################################
		//TAB 1
		Tab tabOne = new Tab();
		tabOne.setText("Record Contacts");
		
		//HBox t1r1 = tab 1, row 1
		HBox t1r1 = new HBox(10);
		t1r1.getChildren().addAll(title);
		t1r1.setAlignment(Pos.TOP_CENTER);
		t1r1.setPadding(new Insets(20, 20, 20,20));
		//HBox t1r2 = tab 1, row 2
		HBox t1r2 = new HBox(10);
		t1r2.getChildren().addAll(fNameLabel);
		t1r2.getChildren().addAll(fNameTextArea);
		t1r2.setAlignment(Pos.CENTER);
		t1r2.setPadding(new Insets(20, 20, 20, 20));
		//HBox t1r3 = tab 1, row 3
		HBox t1r3 = new HBox(10);
		t1r3.getChildren().addAll(lNameLabel);
		t1r3.getChildren().addAll(lNameTextArea);
		t1r3.setAlignment(Pos.CENTER);
		t1r3.setPadding(new Insets(20, 20, 20, 20));
		//HBox t1r4 = tab 1, row 4
		HBox t1r4 = new HBox(10);
		t1r4.getChildren().addAll(uniqueIDLabel);
		t1r4.getChildren().addAll(uniqueIDTextArea);
		t1r4.setAlignment(Pos.CENTER);
		t1r4.setPadding(new Insets(20, 20, 20, 20));
		//HBox t1r5 = tab 1, row 5
		HBox t1r5 = new HBox(10);
		t1r5.getChildren().addAll(phoneNumberLabel);
		t1r5.getChildren().addAll(phoneNumberTextArea);
		t1r5.setAlignment(Pos.CENTER);
		t1r5.setPadding(new Insets(20, 20, 20, 20));
		//HBox t1r6 = tab 1, row 6
		HBox t1r6 = new HBox(10);
		t1r6.getChildren().addAll(addButton, removeButton, listButton);
		t1r6.setAlignment(Pos.CENTER);
		t1r6.setPadding(new Insets(20, 20, 20, 20));
		//HBox t1r7 = tab 1, row 7
		HBox t1r7 = new HBox(10);
		t1r7.getChildren().addAll(closeContactsTextArea);
		t1r7.setAlignment(Pos.CENTER);
		//HBox t1r8 = tab 1, row 8
		HBox t1r8 = new HBox(10);
		t1r8.getChildren().addAll(loadButton, saveButton);
		t1r8.setAlignment(Pos.BOTTOM_LEFT);
		//HBox t1r9 = tab 1, row 9
		HBox t1r9 = new HBox(10);
		t1r9.getChildren().addAll(exitButton);
		t1r9.setAlignment(Pos.BOTTOM_RIGHT);
		
		//Define HBox Layout
		VBox t1Layout = new VBox(10);
		t1Layout.setPadding(new Insets(20, 20, 20, 20));
		t1Layout.getChildren().addAll(t1r1, t1r2, t1r3, t1r4, t1r5, t1r6, t1r7, t1r8, t1r9);
		t1Layout.setStyle("-fx-background-color: #C2A1A5;");
		
		//Set tab one layout and content
		tabOne.setContent(t1Layout);
		tabPane.getTabs().add(tabOne);
		
//#############################################################################################################################################################
		//Tab 2
		Tab tabTwo = new Tab();
		tabTwo.setText("Record Close Contacts");
		
		//Tab 2 title
		HBox t2 = new HBox(10);
		t2.getChildren().addAll(title2);
		t2.setAlignment(Pos.TOP_CENTER);
		t2.setPadding(new Insets(20, 20, 20,20));
		//HBox t2r1 = tab 2, row 1
		HBox t2r1 = new HBox(10);
		t2r1.getChildren().addAll(contact1Label);
		t2r1.getChildren().addAll(contact1ComboBox);
		t2r1.setAlignment(Pos.CENTER);
		t2r1.setPadding(new Insets(20, 20, 20, 20));
		//HBox t2r2 = tab 2, row 2
		HBox t2r2 = new HBox(10);
		t2r2.getChildren().addAll(contact2Label);
		t2r2.getChildren().addAll(contact2ComboBox);
		t2r2.setAlignment(Pos.CENTER);
		t2r2.setPadding(new Insets(20, 20, 20, 20));
		//HBox t2r3 = tab 2, row 3
		HBox t2r3 = new HBox(10);
		t2r3.getChildren().addAll(dateLabel);
		t2r3.getChildren().addAll(dateTextArea);
		t2r3.setAlignment(Pos.CENTER);
		t2r3.setPadding(new Insets(20, 20, 20, 20));
		//HBox t2r4 = tab 2, row 4
		HBox t2r4 = new HBox(10);
		t2r4.getChildren().addAll(timeLabel);
		t2r4.getChildren().addAll(timeTextArea);
		t2r4.setAlignment(Pos.CENTER);
		t2r4.setPadding(new Insets(20, 20, 20, 20));
		//HBox t2r5 = tab 2, row 5
		HBox t2r5 = new HBox(10);
		t2r5.getChildren().addAll(reportButton);
		t2r5.setAlignment(Pos.BOTTOM_LEFT);
		//HBox t2r6 = tab 2, row 6
		HBox t2r6 = new HBox(10);
		t2r6.getChildren().addAll(t2exitButton);
		t2r6.setAlignment(Pos.BOTTOM_RIGHT);
		
		//Define HBox Layout
		VBox t2Layout = new VBox(10);
		t2Layout.setPadding(new Insets(70, 70, 70, 70));
		t2Layout.getChildren().addAll(t2, t2r1, t2r2, t2r3, t2r4, t2r5, t2r6);
		t2Layout.setStyle("-fx-background-color: #C2A1A5;");
		
		//Set tab two layout and content
		tabTwo.setContent(t2Layout);
		tabPane.getTabs().add(tabTwo);
		
//#############################################################################################################################################################
		//Tab 3
		Tab tabThree = new Tab();
		tabThree.setText("Covid Positive Contacts");
		//HBox t3r1 = tab 3, row 1
		HBox t3r1 = new HBox(10);
		t3r1.getChildren().addAll(title3);
		t3r1.setAlignment(Pos.TOP_CENTER);
		t3r1.setPadding(new Insets(50, 50, 50, 50));
		//HBox t3r2 = tab 3, row 2
		HBox t3r2 = new HBox(10);
		t3r2.getChildren().addAll(positiveContactsTextArea);
		t3r2.setAlignment(Pos.CENTER);
		t3r2.setPadding(new Insets(50, 50, 50, 50));
		//HBox t3r3 = tab 3, row 3
		HBox t3r3 = new HBox(10);
		t3r3.getChildren().addAll(listPositiveButton, loadPositiveButton, savePositiveButton);
		t3r3.setAlignment(Pos.BOTTOM_LEFT);
		//HBox t3r4 = tab 3, row 4
		HBox t3r4 = new HBox(10);
		t3r4.getChildren().addAll(t3exitButton);
		t3r4.setAlignment(Pos.BOTTOM_RIGHT);
		
		//Define HBox Layout
		VBox t3Layout = new VBox(10);
		t3Layout.setPadding(new Insets(70, 70, 70, 70));
		t3Layout.getChildren().addAll(t3r1, t3r2, t3r3, t3r4);
		t3Layout.setStyle("-fx-background-color: #C2A1A5;");
		
		//Set tab three layout and content
		tabThree.setContent(t3Layout);
		tabPane.getTabs().add(tabThree);

//#############################################################################################################################################################		
		//mainPane settings
		mainPane.setCenter(tabPane);
		mainPane.prefHeightProperty().bind(scene.heightProperty());
		mainPane.prefWidthProperty().bind(scene.widthProperty());
		
		root.getChildren().add(mainPane);
		primaryStage.setScene(scene);
		primaryStage.show();
		
		
		//Styling labels Tab 1
		fNameLabel.setFont(Font.font(java.awt.Font.SERIF, 15));
		lNameLabel.setFont(Font.font(java.awt.Font.SERIF, 15));
		uniqueIDLabel.setFont(Font.font(java.awt.Font.SERIF, 15));
		phoneNumberLabel.setFont(Font.font(java.awt.Font.SERIF, 15));
		title.setFont(Font.font(java.awt.Font.SERIF, 18));
		//Tab 2
		contact1Label.setFont(Font.font(java.awt.Font.SERIF, 15));
		contact2Label.setFont(Font.font(java.awt.Font.SERIF, 15));
		dateLabel.setFont(Font.font(java.awt.Font.SERIF, 15));
		timeLabel.setFont(Font.font(java.awt.Font.SERIF, 15));
		title2.setFont(Font.font(java.awt.Font.SERIF, 18));
		//Tab 3
		title3.setFont(Font.font(java.awt.Font.SERIF, 18));
		
				
		//Styling Buttons Tab 1
		addButton.setFont(Font.font(java.awt.Font.SERIF, 15));
		removeButton.setFont(Font.font(java.awt.Font.SERIF, 15));
		listButton.setFont(Font.font(java.awt.Font.SERIF, 15));
		//Tab 1 
		loadButton.setFont(Font.font(java.awt.Font.SERIF, 18));
		saveButton.setFont(Font.font(java.awt.Font.SERIF, 18));
		exitButton.setFont(Font.font(java.awt.Font.SERIF, 18));
		//Tab 2
		reportButton.setFont(Font.font(java.awt.Font.SERIF, 18));
		t2exitButton.setFont(Font.font(java.awt.Font.SERIF, 18));
		//Tab 3
		listPositiveButton.setFont(Font.font(java.awt.Font.SERIF, 18));
		savePositiveButton.setFont(Font.font(java.awt.Font.SERIF, 18));
		loadPositiveButton.setFont(Font.font(java.awt.Font.SERIF, 18));
		t3exitButton.setFont(Font.font(java.awt.Font.SERIF, 18));
	}
}
