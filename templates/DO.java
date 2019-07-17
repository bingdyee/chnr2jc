package ${package}.${module}.pojo;

/**
 *  ${comments}
 *
 * @author ${author}
 * @date ${datetime}
 */
public class ${className} {

<?py for column in columns: ?>
    /**$column.columnComment */
    private $column.dataType $column.columnName;
<?py #endfor ?>

<?py for column in columns: ?>
    public void set${column.methodName}($column.dataType $column.columnName) {
        this.$column.columnName = $column.columnName;
    }

    public $column.dataType get${column.methodName}() {
        return $column.columnName;
    }

<?py #endfor ?>
}