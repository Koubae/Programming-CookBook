$data = [];
if (count($ids)) {
    $result = $connection->query("SELECT `x`, `y` FROM `values` WHERE `id` IN (" . implode(',', $ids));
    while ($row = $result->fetch_row()) {
        $data[] = $row;
    }
}