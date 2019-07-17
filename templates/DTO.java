package ${package}.${module}.pojo;

import java.io.Serializable;

/**
 *  ${comments}
 *
 * @author ${author}
 * @date ${datetime}
 */
public class ${className}DTO implements Serializable {

    private static final long serialVersionUID = ${serialVersionUID};

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