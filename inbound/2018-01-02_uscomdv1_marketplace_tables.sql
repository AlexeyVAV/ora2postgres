SQL> BEGIN
  2     DBMS_METADATA.set_transform_param (DBMS_METADATA.session_transform, 'STORAGE', FALSE);
  3     DBMS_METADATA.SET_TRANSFORM_PARAM(DBMS_METADATA.SESSION_TRANSFORM,'TABLESPACE',FALSE);
  4     DBMS_METADATA.SET_TRANSFORM_PARAM(DBMS_METADATA.SESSION_TRANSFORM,'SEGMENT_ATTRIBUTES',FALSE);
  5     -- DBMS_METADATA.SET_TRANSFORM_PARAM(DBMS_METADATA.SESSION_TRANSFORM,'CONSTRAINTS_AS_ALTER',true);
  6  
  7     FOR cur IN (select object_name, object_type, owner from dba_objects where owner='MARKETPLACE'
  8                  and object_type='TABLE'  and rownum < 10)
  9     LOOP
 10        DBMS_OUTPUT.put_line ('-- Create DDL for - ' || cur.owner || '.' || cur.object_name);
 11        dbms_output.put_line(DBMS_METADATA.GET_DDL(cur.object_type, cur.object_name,cur.owner) || ';');
 12  	  dbms_output.put_line('/');
 13        DBMS_OUTPUT.put_line ('-- -------------------------------------------------------');
 14     END LOOP;
 15  END;
 16  /
-- Create DDL for - MARKETPLACE.AGGREGATE_FUNCTION_MATRIX                                                                                                                                                                                                                                                                                                                                                                                                                                                           

  CREATE TABLE "MARKETPLACE"."AGGREGATE_FUNCTION_MATRIX" 
   (	"TABLE_NAME" VARCHAR2(30) NOT NULL ENABLE, 
	"PACKAGE_NAME" VARCHAR2(30) NOT NULL ENABLE, 
	 UNIQUE ("TABLE_NAME")
  USING INDEX  ENABLE, 
	 SUPPLEMENTAL LOG GROUP "GGS_639072" ("TABLE_NAME") ALWAYS
   ) ;                                                                                                                                                                                                                                       
/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
-- -------------------------------------------------------                                                                                                                                                                                                                                                                                                                                                                                                                                                          
-- Create DDL for - MARKETPLACE.AGGREGATE_MATRIX                                                                                                                                                                                                                                                                                                                                                                                                                                                                    

  CREATE TABLE "MARKETPLACE"."AGGREGATE_MATRIX" 
   (	"TABLE_NAME" VARCHAR2(30) NOT NULL ENABLE, 
	"DIMENSION_YN" VARCHAR2(1) NOT NULL ENABLE, 
	 CHECK (DIMENSION_YN IN ('Y','N','R')) ENABLE, 
	 SUPPLEMENTAL LOG DATA (ALL) COLUMNS, 
	 CONSTRAINT "AGGREGATE_MATRIX_FK" FOREIGN KEY ("TABLE_NAME")
	  REFERENCES "MARKETPLACE"."AGGREGATE_FUNCTION_MATRIX" ("TABLE_NAME") ENABLE
   ) ;                                                                                                                        
/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
-- -------------------------------------------------------                                                                                                                                                                                                                                                                                                                                                                                                                                                          
-- Create DDL for - MARKETPLACE.APEX$_ACL                                                                                                                                                                                                                                                                                                                                                                                                                                                                           

  CREATE TABLE "MARKETPLACE"."APEX$_ACL" 
   (	"ID" NUMBER NOT NULL ENABLE, 
	"WS_APP_ID" NUMBER NOT NULL ENABLE, 
	"USERNAME" VARCHAR2(255) NOT NULL ENABLE, 
	"PRIV" VARCHAR2(1) NOT NULL ENABLE, 
	"CREATED_ON" DATE NOT NULL ENABLE, 
	"CREATED_BY" VARCHAR2(255) DEFAULT USER NOT NULL ENABLE, 
	"UPDATED_ON" DATE, 
	"UPDATED_BY" VARCHAR2(255), 
	 CONSTRAINT "APEX$_ACL_PRIV_CK" CHECK (priv in ('R','C','A')) ENABLE, 
	 CONSTRAINT "APEX$_ACL_PK" PRIMARY KEY ("ID")
  USING INDEX  ENABLE
   ) ;        
/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
-- -------------------------------------------------------                                                                                                                                                                                                                                                                                                                                                                                                                                                          
-- Create DDL for - MARKETPLACE.APEX$_WS_FILES                                                                                                                                                                                                                                                                                                                                                                                                                                                                      

  CREATE TABLE "MARKETPLACE"."APEX$_WS_FILES" 
   (	"ID" NUMBER, 
	"WS_APP_ID" NUMBER NOT NULL ENABLE, 
	"DATA_GRID_ID" NUMBER, 
	"ROW_ID" NUMBER, 
	"WEBPAGE_ID" NUMBER, 
	"COMPONENT_LEVEL" VARCHAR2(30), 
	"NAME" VARCHAR2(255) NOT NULL ENABLE, 
	"IMAGE_ALIAS" VARCHAR2(255), 
	"IMAGE_ATTRIBUTES" VARCHAR2(255), 
	"CONTENT" BLOB, 
	"CONTENT_LAST_UPDATE" DATE, 
	"MIME_TYPE" VARCHAR2(255) NOT NULL ENABLE, 
	"CONTENT_CHARSET" VARCHAR2(255), 
	"CONTENT_FILENAME" VARCHAR2(500), 
	"DESCRIPTION"         
VARCHAR2(4000), 
	"CREATED_ON" DATE NOT NULL ENABLE, 
	"CREATED_BY" VARCHAR2(255) DEFAULT USER NOT NULL ENABLE, 
	"UPDATED_ON" DATE, 
	"UPDATED_BY" VARCHAR2(255), 
	 CONSTRAINT "APEX$_WS_FILES_CL_CK" CHECK (component_level in ('WEBSHEET','ROW','WORKSPACE','WEBPAGE')) ENABLE, 
	 CONSTRAINT "APEX$_WS_FILES_PK" PRIMARY KEY ("ID")
  USING INDEX  ENABLE, 
	 CONSTRAINT "APEX$_WS_FILES_FK" FOREIGN KEY ("ROW_ID")
	  REFERENCES "MARKETPLACE"."APEX$_WS_ROWS" ("ID") ON DELETE CASCADE ENABLE
   ) ;         
/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
-- -------------------------------------------------------                                                                                                                                                                                                                                                                                                                                                                                                                                                          
-- Create DDL for - MARKETPLACE.APEX$_WS_HISTORY                                                                                                                                                                                                                                                                                                                                                                                                                                                                    

  CREATE TABLE "MARKETPLACE"."APEX$_WS_HISTORY" 
   (	"ROW_ID" NUMBER NOT NULL ENABLE, 
	"WS_APP_ID" NUMBER NOT NULL ENABLE, 
	"DATA_GRID_ID" NUMBER NOT NULL ENABLE, 
	"COLUMN_NAME" VARCHAR2(255), 
	"OLD_VALUE" VARCHAR2(4000), 
	"NEW_VALUE" VARCHAR2(4000), 
	"APPLICATION_USER_ID" VARCHAR2(255), 
	"CHANGE_DATE" DATE
   ) ;                                                                                                                                                                                
/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
-- -------------------------------------------------------                                                                                                                                                                                                                                                                                                                                                                                                                                                          
-- Create DDL for - MARKETPLACE.APEX$_WS_LINKS                                                                                                                                                                                                                                                                                                                                                                                                                                                                      

  CREATE TABLE "MARKETPLACE"."APEX$_WS_LINKS" 
   (	"ID" NUMBER, 
	"WS_APP_ID" NUMBER NOT NULL ENABLE, 
	"DATA_GRID_ID" NUMBER, 
	"ROW_ID" NUMBER, 
	"WEBPAGE_ID" NUMBER, 
	"COMPONENT_LEVEL" VARCHAR2(30), 
	"TAGS" VARCHAR2(4000), 
	"SHOW_ON_HOMEPAGE" VARCHAR2(1), 
	"LINK_NAME" VARCHAR2(255) NOT NULL ENABLE, 
	"URL" VARCHAR2(4000) NOT NULL ENABLE, 
	"LINK_DESCRIPTION" VARCHAR2(4000), 
	"DISPLAY_SEQUENCE" NUMBER, 
	"CREATED_ON" DATE NOT NULL ENABLE, 
	"CREATED_BY" VARCHAR2(255) DEFAULT USER NOT   
NULL ENABLE, 
	"UPDATED_ON" DATE, 
	"UPDATED_BY" VARCHAR2(255), 
	 CONSTRAINT "APEX$_WS_LINKS_CL_CK" CHECK (component_level in ('WEBSHEET','ROW','WORKSPACE','WEBPAGE')) ENABLE, 
	 CONSTRAINT "APEX$_WS_LINKS_SH_CK" CHECK (show_on_homepage in ('Y','N')) ENABLE, 
	 CONSTRAINT "APEX$_WS_LINKS_PK" PRIMARY KEY ("ID")
  USING INDEX  ENABLE, 
	 CONSTRAINT "APEX$_WS_LINKS_FK" FOREIGN KEY ("ROW_ID")
	  REFERENCES "MARKETPLACE"."APEX$_WS_ROWS" ("ID") ON DELETE CASCADE ENABLE
   ) ;                         
/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
-- -------------------------------------------------------                                                                                                                                                                                                                                                                                                                                                                                                                                                          
-- Create DDL for - MARKETPLACE.APEX$_WS_NOTES                                                                                                                                                                                                                                                                                                                                                                                                                                                                      

  CREATE TABLE "MARKETPLACE"."APEX$_WS_NOTES" 
   (	"ID" NUMBER, 
	"WS_APP_ID" NUMBER NOT NULL ENABLE, 
	"DATA_GRID_ID" NUMBER, 
	"ROW_ID" NUMBER, 
	"WEBPAGE_ID" NUMBER, 
	"COMPONENT_LEVEL" VARCHAR2(30), 
	"CONTENT" CLOB, 
	"CREATED_ON" DATE NOT NULL ENABLE, 
	"CREATED_BY" VARCHAR2(255) DEFAULT USER NOT NULL ENABLE, 
	"UPDATED_ON" DATE, 
	"UPDATED_BY" VARCHAR2(255), 
	 CONSTRAINT "APEX$_WS_NOTES_CL_CK" CHECK (component_level in ('WEBSHEET','ROW','WORKSPACE','WEBPAGE')) ENABLE, 
	 CONSTRAINT    
"APEX$_WS_NOTES_PK" PRIMARY KEY ("ID")
  USING INDEX  ENABLE, 
	 CONSTRAINT "APEX$_WS_NOTES_FK" FOREIGN KEY ("ROW_ID")
	  REFERENCES "MARKETPLACE"."APEX$_WS_ROWS" ("ID") ON DELETE CASCADE ENABLE
   ) ;                                                                                                                                                                                                                                                                                                           
/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
-- -------------------------------------------------------                                                                                                                                                                                                                                                                                                                                                                                                                                                          
-- Create DDL for - MARKETPLACE.APEX$_WS_ROWS                                                                                                                                                                                                                                                                                                                                                                                                                                                                       

  CREATE TABLE "MARKETPLACE"."APEX$_WS_ROWS" 
   (	"ID" NUMBER NOT NULL ENABLE, 
	"WS_APP_ID" NUMBER NOT NULL ENABLE, 
	"DATA_GRID_ID" NUMBER NOT NULL ENABLE, 
	"UNIQUE_VALUE" VARCHAR2(255), 
	"TAGS" VARCHAR2(4000), 
	"PARENT_ROW_ID" NUMBER, 
	"OWNER" VARCHAR2(255), 
	"GEOCODE" VARCHAR2(512), 
	"LOAD_ORDER" NUMBER, 
	"CHANGE_COUNT" NUMBER, 
	"CREATED_ON" DATE NOT NULL ENABLE, 
	"CREATED_BY" VARCHAR2(255) DEFAULT USER NOT NULL ENABLE, 
	"UPDATED_ON" DATE, 
	"UPDATED_BY" VARCHAR2(255), 
	"C001"  
VARCHAR2(4000), 
	"C002" VARCHAR2(4000), 
	"C003" VARCHAR2(4000), 
	"C004" VARCHAR2(4000), 
	"C005" VARCHAR2(4000), 
	"C006" VARCHAR2(4000), 
	"C007" VARCHAR2(4000), 
	"C008" VARCHAR2(4000), 
	"C009" VARCHAR2(4000), 
	"C010" VARCHAR2(4000), 
	"C011" VARCHAR2(4000), 
	"C012" VARCHAR2(4000), 
	"C013" VARCHAR2(4000), 
	"C014" VARCHAR2(4000), 
	"C015" VARCHAR2(4000), 
	"C016" VARCHAR2(4000), 
	"C017" VARCHAR2(4000), 
	"C018" VARCHAR2(4000), 
	"C019" VARCHAR2(4000), 
	"C020" VARCHAR2(4000), 
	"C021" 
VARCHAR2(4000), 
	"C022" VARCHAR2(4000), 
	"C023" VARCHAR2(4000), 
	"C024" VARCHAR2(4000), 
	"C025" VARCHAR2(4000), 
	"C026" VARCHAR2(4000), 
	"C027" VARCHAR2(4000), 
	"C028" VARCHAR2(4000), 
	"C029" VARCHAR2(4000), 
	"C030" VARCHAR2(4000), 
	"C031" VARCHAR2(4000), 
	"C032" VARCHAR2(4000), 
	"C033" VARCHAR2(4000), 
	"C034" VARCHAR2(4000), 
	"C035" VARCHAR2(4000), 
	"C036" VARCHAR2(4000), 
	"C037" VARCHAR2(4000), 
	"C038" VARCHAR2(4000), 
	"C039" VARCHAR2(4000), 
	"C040" VARCHAR2(4000), 
	"C041" 
VARCHAR2(4000), 
	"C042" VARCHAR2(4000), 
	"C043" VARCHAR2(4000), 
	"C044" VARCHAR2(4000), 
	"C045" VARCHAR2(4000), 
	"C046" VARCHAR2(4000), 
	"C047" VARCHAR2(4000), 
	"C048" VARCHAR2(4000), 
	"C049" VARCHAR2(4000), 
	"C050" VARCHAR2(4000), 
	"N001" NUMBER, 
	"N002" NUMBER, 
	"N003" NUMBER, 
	"N004" NUMBER, 
	"N005" NUMBER, 
	"N006" NUMBER, 
	"N007" NUMBER, 
	"N008" NUMBER, 
	"N009" NUMBER, 
	"N010" NUMBER, 
	"N011" NUMBER, 
	"N012" NUMBER, 
	"N013" NUMBER, 
	"N014" NUMBER, 
	"N015" NUMBER,     

	"N016" NUMBER, 
	"N017" NUMBER, 
	"N018" NUMBER, 
	"N019" NUMBER, 
	"N020" NUMBER, 
	"N021" NUMBER, 
	"N022" NUMBER, 
	"N023" NUMBER, 
	"N024" NUMBER, 
	"N025" NUMBER, 
	"N026" NUMBER, 
	"N027" NUMBER, 
	"N028" NUMBER, 
	"N029" NUMBER, 
	"N030" NUMBER, 
	"N031" NUMBER, 
	"N032" NUMBER, 
	"N033" NUMBER, 
	"N034" NUMBER, 
	"N035" NUMBER, 
	"N036" NUMBER, 
	"N037" NUMBER, 
	"N038" NUMBER, 
	"N039" NUMBER, 
	"N040" NUMBER, 
	"N041" NUMBER, 
	"N042" NUMBER, 
	"N043" NUMBER, 
	"N044" NUMBER,        

	"N045" NUMBER, 
	"N046" NUMBER, 
	"N047" NUMBER, 
	"N048" NUMBER, 
	"N049" NUMBER, 
	"N050" NUMBER, 
	"D001" DATE, 
	"D002" DATE, 
	"D003" DATE, 
	"D004" DATE, 
	"D005" DATE, 
	"D006" DATE, 
	"D007" DATE, 
	"D008" DATE, 
	"D009" DATE, 
	"D010" DATE, 
	"D011" DATE, 
	"D012" DATE, 
	"D013" DATE, 
	"D014" DATE, 
	"D015" DATE, 
	"D016" DATE, 
	"D017" DATE, 
	"D018" DATE, 
	"D019" DATE, 
	"D020" DATE, 
	"D021" DATE, 
	"D022" DATE, 
	"D023" DATE, 
	"D024" DATE, 
	"D025" DATE, 
	"D026" DATE, 
	"D027"
DATE, 
	"D028" DATE, 
	"D029" DATE, 
	"D030" DATE, 
	"D031" DATE, 
	"D032" DATE, 
	"D033" DATE, 
	"D034" DATE, 
	"D035" DATE, 
	"D036" DATE, 
	"D037" DATE, 
	"D038" DATE, 
	"D039" DATE, 
	"D040" DATE, 
	"D041" DATE, 
	"D042" DATE, 
	"D043" DATE, 
	"D044" DATE, 
	"D045" DATE, 
	"D046" DATE, 
	"D047" DATE, 
	"D048" DATE, 
	"D049" DATE, 
	"D050" DATE, 
	"CLOB001" CLOB, 
	"SEARCH_CLOB" CLOB, 
	 CONSTRAINT "APEX$_WS_ROWS_PK" PRIMARY KEY ("ID")
  USING INDEX  ENABLE
   ) ;                             
/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
-- -------------------------------------------------------                                                                                                                                                                                                                                                                                                                                                                                                                                                          
-- Create DDL for - MARKETPLACE.APEX$_WS_TAGS                                                                                                                                                                                                                                                                                                                                                                                                                                                                       

  CREATE TABLE "MARKETPLACE"."APEX$_WS_TAGS" 
   (	"ID" NUMBER, 
	"WS_APP_ID" NUMBER NOT NULL ENABLE, 
	"DATA_GRID_ID" NUMBER, 
	"ROW_ID" NUMBER, 
	"WEBPAGE_ID" NUMBER, 
	"COMPONENT_LEVEL" VARCHAR2(30), 
	"TAG" VARCHAR2(4000), 
	"CREATED_ON" DATE NOT NULL ENABLE, 
	"CREATED_BY" VARCHAR2(255) DEFAULT USER NOT NULL ENABLE, 
	"UPDATED_ON" DATE, 
	"UPDATED_BY" VARCHAR2(255), 
	 CONSTRAINT "APEX$_WS_TAGS_CL_CK" CHECK (component_level in ('WEBSHEET','ROW','WORKSPACE','WEBPAGE')) ENABLE, 
	 CONSTRAINT
"APEX$_WS_TAGS_PK" PRIMARY KEY ("ID")
  USING INDEX  ENABLE, 
	 CONSTRAINT "APEX$_WS_TAGS_FK" FOREIGN KEY ("ROW_ID")
	  REFERENCES "MARKETPLACE"."APEX$_WS_ROWS" ("ID") ON DELETE CASCADE ENABLE
   ) ;                                                                                                                                                                                                                                                                                                             
/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
-- -------------------------------------------------------                                                                                                                                                                                                                                                                                                                                                                                                                                                          

PL/SQL procedure successfully completed.

SQL> spo off
