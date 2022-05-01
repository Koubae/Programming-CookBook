-- sqlite
-- INFO: https://www.sqlitetutorial.net/sqlite-vacuum/


VACUUM;

-- enables full auto-vacuum mode
PRAGMA auto_vacuum = FULL;

--  disables auto-vacuum mode
PRAGMA auto_vacuum = NONE;

-- enable incremental vacuum
PRAGMA auto_vacuum = INCREMENTAL;

-- syntax of the VACUUM with INTO clause:
VACUUM schema-name INTO filename;

VACUUM main INTO 'c:\sqlite\db\chinook_backup.db';